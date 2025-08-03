import os

import pymupdf


if not os.path.exists("./Import"):
	os.mkdir("./Import")
import_dir: os.path = os.path.abspath("./Import")

if not os.path.exists("./bin"):
	os.mkdir("./bin")
bin_dir: os.path = os.path.abspath("./bin")


class PDF:
	def __init__(self, file_path):
		self.doc = pymupdf.open(file_path)
		metadata: dict = self.doc.metadata
		
		if metadata["title"] == "":
			print("Invalid PDF. Only non-anonymous PDFs from Paizo are supported.")
			return
			
		self.season: int = int(metadata["title"][-9:-7])
		self.scenario: int = int(metadata["title"][-7:-5])
		print(f"Extracting PDF for Season {self.season}, Scenario {self.scenario}")
		
		self.output_dir: os.path = os.path.join(bin_dir, f"S{self.season}S{self.scenario}")
		if not os.path.exists(self.output_dir):
			os.mkdir(self.output_dir)
		
		self.asset_dir: os.path = os.path.join(self.output_dir, "Assets")
		if not os.path.exists(self.asset_dir):
			os.mkdir(self.asset_dir)
			
		self.img_dir: os.path = os.path.join(self.asset_dir, "Extracted Images")
		if not os.path.exists(self.img_dir):
			os.mkdir(self.img_dir)
		
		self.extract_images()
		self.extract_blocks()
	
	def extract_blocks(self):
		output_file = os.path.join(self.output_dir, "extracted_blocks.txt")
		out = open(output_file, "wb")
		for page in self.doc:
			blocks = page.get_text("blocks").encode("utf8")
			print(blocks)
	
	def extract_images(self):
		for page_num in range(len(self.doc)):
			page = self.doc.load_page(page_num)
			image_list = page.get_images(full=True)
			
			for img_index, img_info in enumerate(image_list):
				xref = img_info[0]
				base_image = self.doc.extract_image(xref)
				
				image_bytes = base_image["image"]
				image_ext = base_image["ext"]
				
				file_path = os.path.join(self.img_dir, f"extracted_image_page{page_num+1}_img{img_index+1}.{image_ext}")
				with open(file_path, "wb") as img_file:
					img_file.write(image_bytes)
			

if __name__ == "__main__":
	pdf2 = PDF(os.path.join(import_dir, "Scenario #05 - Trailblazers Bounty.pdf"))
	pdf = PDF(os.path.join(import_dir, "PZOPFS0105E.pdf"))
