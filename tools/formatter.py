import json
import os

import FreeSimpleGUI as sg


class Paragraph:
	def __init__(self, line_list: list[str], size: float, color: int, font: str):
		self.text: str = ""
		self.size: float = size
		self.color: int = color
		self.font: str = font
		
		for line in line_list:
			self.text += line
	
	def compose(self) -> sg.Text:
		paragraph = sg.Text(self.text)
		
		return paragraph


if __name__ == "__main__":
	bin_dir = os.path.abspath("../bin")
	modules_dir = os.path.join(bin_dir, "Modules")
	season_dir = os.path.join(modules_dir, "Season 1")
	scenario_dir = os.path.join(season_dir, "Scenario 7")
	pages_dir = os.path.join(scenario_dir, "Pages")
	file_path = os.path.join(pages_dir, "page 0.json")
	page_list: list = []

	for root, _, files in os.walk(pages_dir):
		for file in files:
			file_path = os.path.join(root, file)
			
			with open(file_path, "r") as file:
				data = json.load(file)
			
			page_list.append(data)
	
	for page_index, page in enumerate(page_list):
		for block_index, block in enumerate(page["blocks"]):
			print(f"Page {page_index}, block: {block_index} {block}")
