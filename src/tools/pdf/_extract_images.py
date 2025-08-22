import os
from src.config._directory import DIRECTORY, make_directory


def run(doc, season, scenario, tier = None):
	if tier:
		scenario_dir = os.path.join(DIRECTORY[season], f"Scenario {scenario} ({tier})")
		print(f"Extracting images from Season: {season}, Scenario: {scenario} ({tier})")
	else:
		scenario_dir = os.path.join(DIRECTORY[season], f"Scenario {scenario}")
		print(f"Extracting images from Season: {season}, Scenario: {scenario}")
	make_directory(scenario_dir)
	image_dir = os.path.join(scenario_dir, "Images")
	make_directory(image_dir)
	
	
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
