import json
import os
import pymupdf
import src.console.console as console


def run(directory: dict):
	file_errors: list = []
	
	for root, dirs, files in os.walk(directory["import"]):
		number_of_files = int(len(files))
		print(number_of_files)
		current_file = 1
		progress: float = (current_file / number_of_files) * 100
		
		display(progress, file_errors)
		
		for file in files:
			if file.endswith(".pdf"):
				display(progress, file_errors)
				file_path = os.path.join(root, file)
				file_name = os.path.basename(file_path)
				file_name = os.path.splitext(file_name)[0]
				
				doc = pymupdf.open(file_path)
				
				try:
					tier: str = str(doc.metadata["title"].replace(").pdf", "").replace("(", "").split(" ")[-1])
				except ValueError:
					tier = None
				
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
					file_errors.append(file_name)
					current_file += 1
					continue
				
				season_dir = os.path.join(directory["modules"], f"{season}")
				if not os.path.exists(season_dir):
					os.mkdir(season_dir)
				
				if tier is not None:
					scenario_dir = os.path.join(season_dir, f"Scenario {scenario} ({tier})")
				else:
					scenario_dir = os.path.join(season_dir, f"Scenario {scenario}")
				
				if not os.path.exists(scenario_dir):
					os.mkdir(scenario_dir)
				
				_extract_text(doc, scenario_dir)
				_extract_images(doc, scenario_dir)
				doc.close()
				os.remove(file_path)
				
				current_file += 1
				progress = (current_file / number_of_files) * 100
	
	display(100, file_errors)
	main_loop()


def display(progress, errors):
	segment_length: int = 4
	
	console.clear()
	print("DM's Halfling - Importing PDFs\n\n")
	
	progress_bar: str = "["
	
	i = 0
	while i < progress:
		progress_bar += "▓"
		i += segment_length
	
	while i < 100:
		progress_bar += " "
		i += segment_length

	progress_bar += "]"
	
	print(progress_bar)
	print()
	if errors:
		for error in errors:
			print(error)
	
	if progress == 100:
		print("[B]ack | [Q]uit")
	
	
def main_loop():
	while(True):
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
	

def _extract_text(doc, scenario_dir):
	output_file = os.path.join(scenario_dir, "output.json")
	
	line_dict: dict = {}
	
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


def _extract_images(doc, scenario_dir):
	image_dir = os.path.join(scenario_dir, "Images")
	
	if not os.path.exists(image_dir):
		os.mkdir(image_dir)
		
	for page_num in range(len(doc)):
		page = doc.load_page(page_num)
		image_list = page.get_images(full = True)
		
		for img_index, img_info in enumerate(image_list):
			xref = img_info[0]
			
			base_image = doc.extract_image(xref)
			
			image_bytes = base_image["image"]
			image_ext = base_image["ext"]
			
			file_path = os.path.join(image_dir, f"{xref}.{image_ext}")
			
			with open(file_path, "wb") as img_file:
				img_file.write(image_bytes)
