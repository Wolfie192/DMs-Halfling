import json
import os

import FreeSimpleGUI as fsg


class Title:
	def __init__(self, text, *args, **kwargs):
		self.element = fsg.Text(text, font = ("any", 32), justification = "center", expand_x = True)
	

class SectionHeader:
	def __init__(self, text: str):
		self.element = fsg.Text(text, font = ("any", 24))


class SubSectionHeader:
	def __init__(self, text: str):
		self.element = fsg.Text(text, font = ("any", 18))


class Paragraph:
	def __init__(self, text: list):
		text_string: str = ""
		for line in text:
			text_string += line
		
		self.element = fsg.Text(text_string)
			


if __name__ == "__main__":
	fsg.theme("DarkGrey")
	bin_dir = os.path.abspath("./bin")
	scenario_dir = os.path.join(bin_dir, "S01S01")
	text_file = os.path.join(scenario_dir, "extracted_text.json")
	
	with open(text_file, "r", encoding = "utf-8") as f:
		pdf_content = json.load(f)
	
	title = Title(pdf_content["blocks"][0]["lines"][2]["spans"][0]["text"])
	#TODO Look through the rest of the dict to make sure it is in a readable format and can be used for the rest of the information.
	
	layout = [
		[title.element]
	]
	
	window = fsg.Window("test window", layout, resizable = True)
	
	while True:
		event, values = window.read(timeout = 1000)
		
		if event == fsg.WIN_CLOSED:
			break
	
	window.close()
