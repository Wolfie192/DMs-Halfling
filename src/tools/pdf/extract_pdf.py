import pymupdf
import src.tools.pdf._extract_dict as _extract_dict
import src.tools.pdf._extract_images as _extract_images


def run(pdf_file_path):
	doc = pymupdf.open(pdf_file_path)
	
	if doc.metadata["title"] == "":
		#TODO figure out how to handle an error of the file not being compatible.
		return None

	try:
		tier: str = str(doc.metadata["title"].replace(").pdf", "").replace("(", "").split(" ")[-1])
	except ValueError:
		#TODO figure out how to handle an error of the file not being compatible.
		return None
	
	try:
		if int(doc.metadata["title"][6:8]) == 60 or int(doc.metadata["title"][6:8]) == 61:
			season: str = f"Season {doc.metadata["title"][5:7].replace("0", "")}"
			scenario: int = int(doc.metadata["title"][7:9])
		elif doc.metadata["title"][5:8] == "Q00":
			season: str = "Quests"
			scenario: int = int(doc.metadata["title"][8:10])
		elif doc.metadata["title"][5:7] == "Q0":
			season: str = "Quests"
			scenario: int = int(doc.metadata["title"][7:9])
		elif doc.metadata["title"][5] == "B":
			season: str = "Bounties"
			scenario: int = int(doc.metadata["title"][8:10].replace("E", ""))
		else:
			season: str = f"Season {doc.metadata["title"][6:8].replace("0", "")}"
			scenario: int = int(doc.metadata["title"][8:10])
	except ValueError:
		#TODO figure out how to handle an error of the file not being compatible.
		return None
	
	try:
		int(tier.split("-")[0])
	except ValueError:
		tier = None

	_extract_images.run(doc, season, scenario, tier)
	_extract_dict.run(doc, season, scenario, tier)
	
	return None


if __name__ == "__main__":
	import os
	
	pdfs_dir = "D:\\ProgrammingProjects\\Python\\DMs-Halfling\\pdfs_for_upload_testing"
	
	for root, _, files in os.walk(pdfs_dir):
		for file in files:
			file_path = os.path.join(root, file)
			run(file_path)
