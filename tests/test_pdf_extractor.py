import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


# The extractor's control flow is tested with document doubles, so PyMuPDF does
# not need to be installed merely to import this module in the test environment.
pymupdf_stub = types.ModuleType("pymupdf")
pymupdf_stub.TEXTFLAGS_DICT = 3
pymupdf_stub.TEXT_PRESERVE_IMAGES = 1
with patch.dict(sys.modules, {"pymupdf": pymupdf_stub}):
    from tools import pdf_extractor


class PdfExtractorTests(unittest.TestCase):
    def test_extract_file_routes_scenario_and_closes_document(self):
        document = MagicMock()
        document.metadata = {"title": "prefix0107 1-4"}

        with tempfile.TemporaryDirectory() as temp_dir:
            modules_dir = Path(temp_dir) / "Modules"
            modules_dir.mkdir()
            expected_output = modules_dir / "Season 1" / "Scenario 7(1-4)"

            with (
                patch.object(pdf_extractor.pymupdf, "open", return_value=document),
                patch.object(pdf_extractor, "extract_images") as extract_images,
                patch.object(pdf_extractor, "extract_text") as extract_text,
            ):
                result = pdf_extractor.extract_file({"Modules": str(modules_dir)}, "scenario.pdf")

        self.assertEqual(result, "")
        extract_images.assert_called_once_with(str(expected_output), document, "Season 1", 7)
        extract_text.assert_called_once_with(str(expected_output), document)
        document.close.assert_called_once_with()

    def test_extract_file_rejects_missing_title_and_closes_document(self):
        document = MagicMock()
        document.metadata = {"title": None}

        with patch.object(pdf_extractor.pymupdf, "open", return_value=document):
            result = pdf_extractor.extract_file({"Modules": "unused"}, "unsigned.pdf")

        self.assertEqual(result, "Only official Paizo PDFs are accepted.")
        document.close.assert_called_once_with()

    def test_extract_file_rejects_malformed_title_and_closes_document(self):
        document = MagicMock()
        document.metadata = {"title": "prefixABCD"}

        with tempfile.TemporaryDirectory() as temp_dir:
            modules_dir = Path(temp_dir) / "Modules"
            modules_dir.mkdir()
            with patch.object(pdf_extractor.pymupdf, "open", return_value=document):
                result = pdf_extractor.extract_file({"Modules": str(modules_dir)}, "malformed.pdf")

            self.assertEqual(list(modules_dir.iterdir()), [])

        self.assertIn("Could not parse season and scenario", result)
        document.close.assert_called_once_with()

    def test_extract_text_writes_span_data_as_json(self):
        span = {
            "size": 12.0,
            "font": "TestFont",
            "color": 123,
            "alpha": 255,
            "text": "Read aloud text",
            "flags": 0,
            "bidi": 0,
            "char_flags": 0,
            "ascender": 1.0,
            "descender": -0.2,
            "origin": (0, 0),
            "bbox": (0, 0, 1, 1),
        }
        line = {
            "wmode": 0,
            "dir": (1, 0),
            "bbox": (0, 0, 1, 1),
            "spans": [span],
        }
        block = {
            "bbox": (0, 0, 1, 1),
            "type": 0,
            "number": 0,
            "lines": [line],
        }
        page = MagicMock()
        page.get_text.return_value = {"width": 100, "height": 100, "blocks": [block]}
        document = MagicMock()
        document.__len__.return_value = 1
        document.__getitem__.return_value = page

        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_extractor.extract_text(temp_dir, document)
            output = json.loads((Path(temp_dir) / "output.json").read_text())

        self.assertEqual(
            output["0.0.0.0"],
            {"size": 12.0, "font": "TestFont", "color": 123, "alpha": 255, "text": "Read aloud text"},
        )
        page.get_text.assert_called_once_with("dict", flags=2)

    def test_extract_images_writes_image_bytes(self):
        page = MagicMock()
        page.get_images.return_value = [(42,)]
        document = MagicMock()
        document.__len__.return_value = 1
        document.load_page.return_value = page
        document.extract_image.return_value = {"image": b"image-data", "ext": "png"}

        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_extractor.extract_images(temp_dir, document, "Season 1", 7)
            image_path = Path(temp_dir) / "Assets" / "Images" / "42.png"

            self.assertEqual(image_path.read_bytes(), b"image-data")

        page.get_images.assert_called_once_with(full=True)
        document.extract_image.assert_called_once_with(42)


if __name__ == "__main__":
    unittest.main()
