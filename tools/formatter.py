import json
import os

import FreeSimpleGUI as sg


class Paragraph:
	def __init__(self, file_path, line_list: list):
		self.file_path = file_path
		self.text = ""
		
		with open(self.file_path, "r") as file:
			self.data = json.load(file)
		
		for line in line_list:
			if isinstance(line, tuple):
				p = line[0].split(".")[0]
				b = line[0].split(".")[1]
				i = int(line[0].split(".")[2])
				while str(i) <= line[1].split(".")[2]:
					self.text += data[f"{p}.{b}.{str(i)}"]["text"]
					i += 1
			else:
				self.text += line["text"]
	
	def compose(self) -> sg.Text:
		return sg.Text(self.text)


if __name__ == "__main__":
	bin_dir = os.path.abspath("../bin")
	modules_dir = os.path.join(bin_dir, "Modules")
	season_dir = os.path.join(modules_dir, "Season 1")
	scenario_dir = os.path.join(season_dir, "Scenario 7")
	file_path = os.path.join(scenario_dir, "output.json")
	
	with open(file_path, "r") as file:
		data = json.load(file)
	
	paragraph = Paragraph(file_path, [("2.12.1", "2.12.8")])
	
	print(paragraph.text)
