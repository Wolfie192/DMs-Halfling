import json
import os
import pymupdf

import tools.ModuleManager as mm


def check_dir(dir_path):
	if not os.path.exists(dir_path):
		os.mkdir(dir_path)


def extract_file(directories, file_path) -> str:
	doc = pymupdf.open(file_path)
	
	if doc.metadata["title"] == "":
		error = "Only official Paizo PDFs are accepted."
		return error
	
	try:
		tier: str = str(doc.metadata["title"].replace(").pdf", "").split(" ")[-1])
	except ValueError:
		print(f"Error, invalid value, {doc.metadata["title"][13:16]} received")
		
	try:	
		if doc.metadata["title"][6:8] == "60" or doc.metadata["title"][6:8] == "61":
			season_str: str = doc.metadata["title"][5:7]
			scenario_str: str = doc.metadata["title"][7:9]
		elif doc.metadata["title"][5:8] == "Q00":
			season_str: str = "0"
			scenario_str: str = doc.metadata["title"][8:10]
		elif doc.metadata["title"][5:7] == "Q0":
			season_str: str = "0"
			scenario_str: str = doc.metadata["title"][7:9]
		elif doc.metadata["title"][5] == "B":
			season_str: str = "99"
			scenario_str: str = doc.metadata["title"][8:10].replace("E", "")
		else:
			season_str: str = doc.metadata["title"][6:8]
			scenario_str: str = doc.metadata["title"][8:10]
		
		season: int = int(season_str)
		scenario: int = int(scenario_str)
	except ValueError:
		print(f"Error, invalid value, ({season_str}, {scenario_str}) received")

	match season:
		case 0:
			season_out = "Quests"
			scenario_out = f"Quest {scenario}"
		case 99:
			season_out = "Bounties"
			scenario_out = f"Bounty {scenario}"
		case _:
			season_out = f"Season {season}"
			scenario_out = f"Scenario {scenario}"
	
	print(season_out, scenario)
	
	season_dir = os.path.join(directories["Modules"], season_out)
	check_dir(season_dir)
	
	try:
		int(tier.split("-")[0])
		output_dir = os.path.join(season_dir, scenario_out + f"({tier})")
	except ValueError:
		output_dir = os.path.join(season_dir, scenario_out)
	check_dir(output_dir)
	
	#print(f"Extracting images from ({season}, {scenario})")
	extract_images(output_dir, doc, season_out, scenario)
	#print(f"Extracting text from ({season}, {scenario})")
	# noinspection PyTypeChecker
	extract_text(output_dir, doc)
	
	return ""


def extract_images(output_dir, doc, season, scenario):
	asset_dir = os.path.join(output_dir, "Assets")
	check_dir(asset_dir)
	
	img_dir = os.path.join(asset_dir, "Images")
	check_dir(img_dir)
	
	for page_num in range(len(doc)):
		page = doc.load_page(page_num)
		image_list = page.get_images(full = True)
		
		for img_index, img_info in enumerate(image_list):
			xref = img_info[0]
			
			base_image = doc.extract_image(xref)
			
			image_bytes = base_image["image"]
			image_ext = base_image["ext"]
			
			file_path = os.path.join(img_dir, f"{xref}.{image_ext}")
			
			with open(file_path, "wb") as img_file:
				img_file.write(image_bytes)


def extract_text(output_dir, doc):
	page_list: list = []
	
	line_dict: dict = {f"Page.Block.Line": {
		"size": "float",
		"font": "string",
		"color": "int",
		"alpha": "int",
		"text": "string"
	}}
	
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
					
					line_dict[f"{page_index}.{block_index}.{line_index}"] = {
						"size": span["size"],
						"font": span["font"],
						"color": span["color"],
						"alpha": span["alpha"],
						"text": span["text"]
					}
		
	with open(os.path.join(output_dir, f"output.json"), "w") as file:
		json.dump(line_dict, file, indent = 2)


if __name__ == "__main__":
	pass
