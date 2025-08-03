import os
import shutil

import pymupdf


def get_bin_dir() -> os.path:
	if not os.path.exists("./bin"):
		os.mkdir("./bin")
	bin_dir: os.path = os.path.abspath("./bin")
	return bin_dir


def extract_file(file_path):
	bin_dir: os.path = get_bin_dir()
	doc = pymupdf.open(file_path)
	
	if doc.metadata["title"] == "":
		print("Invalid PDF. Only non-anonymous PDFs from Paizo are supported.")
		return
	
	season: int = int(doc.metadata["title"][-9:-7])
	scenario: int = int(doc.metadata["title"][-7:-5])
	print(f"Extracting PDF for Season {season}, Scenario {scenario}")
	
	output_dir: os.path = os.path.join(bin_dir, f"S{season}S{scenario}")
	if not os.path.exists(output_dir):
		os.mkdir(output_dir)

	asset_dir: os.path = os.path.join(output_dir, "Assets")
	if not os.path.exists(asset_dir):
		os.mkdir(asset_dir)
		
	img_dir: os.path = os.path.join(asset_dir, "Extracted Images")
	if not os.path.exists(img_dir):
		os.mkdir(img_dir)
	
	shutil.copy(file_path, output_dir)
	extract_images(doc, img_dir)

def extract_images(doc, img_dir):
	for page_num in range(len(doc)):
		page = doc.load_page(page_num)
		image_list = page.get_images(full=True)
		
		for img_index, img_info in enumerate(image_list):
			xref = img_info[0]
			base_image = doc.extract_image(xref)
			
			image_bytes = base_image["image"]
			image_ext = base_image["ext"]
			
			file_path = os.path.join(img_dir, f"extracted_image_page{page_num+1}_img{img_index+1}.{image_ext}")
			with open(file_path, "wb") as img_file:
				img_file.write(image_bytes)
		

if __name__ == "__main__":
	pass
