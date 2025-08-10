import os
import pymupdf
import shutil


def check_dir(dir_path):
	if not os.path.exists(dir_path):
		os.mkdir(dir_path)


def get_scenario_num(file_path):
	doc = pymupdf.open(file_path)
		
	season: str = str(doc.metadata["title"][-9:-7])
	scenario: str = str(doc.metadata["title"][-7:-5])
	
	return season, scenario
		

def extract_file(root_dir, file_path) -> bool:
	doc = pymupdf.open(file_path)
	
	if doc.metadata["title"] == "":
		return False
	
	season, scenario = get_scenario_num(file_path)
	
	output_dir = os.path.join(root_dir, f"S{season}S{scenario}")
	check_dir(output_dir)
	
	asset_dir = os.path.join(output_dir, "Assets")
	check_dir(asset_dir)
	
	img_dir = os.path.join(asset_dir, "Images")
	check_dir(img_dir)
	
	shutil.copy(file_path, output_dir)
	extract_images(doc, img_dir)
	extract_text(doc, output_dir)
	
	return True


def extract_images(doc, img_dir):
	for page_num in range(len(doc)):
		page = doc.load_page(page_num)
		image_list = page.get_images(full = True)
		
		for img_index, img_info in enumerate(image_list):
			xref = img_info[0]
			base_image = doc.extract_image(xref)
			
			image_bytes = base_image["image"]
			image_ext = base_image["ext"]
			
			file_path = os.path.join(img_dir, f"extracted_image_page{page_num+1}_img{img_index+1}.{image_ext}")
			
			with open(file_path, "wb") as img_file:
				img_file.write(image_bytes)


def extract_text(doc, output_dir):
	output_file = os.path.join(output_dir, "extracted_text.txt")
	
	with open(output_file, "ab") as f:
		for page in doc:
			text = page.get_text().encode("utf-8")
			f.write(text)
			f.write(bytes((12, )))


if __name__ == "__main__":
	pass
