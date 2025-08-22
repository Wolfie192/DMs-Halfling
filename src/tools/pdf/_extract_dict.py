import json
import os
import pymupdf
from src.config._directory import DIRECTORY, make_directory


def run(doc, season, scenario, tier = None):
	if tier:
		output_dir = os.path.join(DIRECTORY[season], f"Scenario {scenario} ({tier})")
		print(f"Extracting text as dict from Season: {season}, Scenario: {scenario} ({tier})")
	else:
		output_dir = os.path.join(DIRECTORY[season], f"Scenario {scenario}")
		print(f"Extracting text as dict from Season: {season}, Scenario: {scenario}")
	make_directory(output_dir)
	
	output_file = os.path.join(output_dir, "output.json")
	
	page_list: list = []
	
	line_dict: dict = {
		"Season": season,
		"Scenario": scenario,
		"Tier": tier,
		"Format": {
			f"Page.Block.Line.Span": {
				"size": "float",
				"font": "string",
				"color": "int",
				"alpha": "int",
				"text": "string"
			}
		}
	}
	
	for page_index in range(len(doc)):
		page = doc[page_index]
		text = page.get_text("dict", flags = pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES)
		
		text.pop("width")
		text.pop("height")
		
		for block_index, block in enumerate(text["blocks"]):
			block.pop("bbox")
			block.pop("type")
			block.pop("number")
			
			for line_index, line in enumerate(block["lines"]):
				line.pop("wmode")
				line.pop("dir")
				line.pop("bbox")
				
				for span_index, span in enumerate(line["spans"]):
					span.pop("flags")
					span.pop("bidi")
					span.pop("char_flags")
					span.pop("ascender")
					span.pop("descender")
					span.pop("origin")
					span.pop("bbox")
					
					line_dict[f"{page_index}.{block_index}.{line_index}.{span_index}"] = {
						"size": span["size"],
						"font": span["font"],
						"color": span["color"],
						"alpha": span["alpha"],
						"text": span["text"]
					}
	
	with open(output_file, "w") as file:
		json.dump(line_dict, file, indent = 2)
