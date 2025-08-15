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
