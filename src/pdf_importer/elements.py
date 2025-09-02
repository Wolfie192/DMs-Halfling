from src.console import console


class Paragraph:
	def __init__(self):
		self.text = None
	
	def add_text(self, *lines):
		for line in lines:
			if self.text is None:
				self.text = line["text"]
			else:
				self.text += line["text"]
	
	def display(self):
		width = console.width()
		output_str: str = ""
		
		words = self.text.split(" ")
		
		for word in words:
			if word == words[0]:
				new_output_str = "     " + word
			else:
				new_output_str = output_str + " " + word
			
			if len(new_output_str) > (width - 5):
				print(output_str)
				output_str = word
			elif word == words[-1]:
				print(new_output_str)
			elif len(new_output_str) < (width - 5):
				output_str = new_output_str


class Section:
	def __init__(self, header = None):
		self.header = header
		self.elements: list = []
	
	def add(self, element, order = None):
		if order is not None:
			self.elements.insert((order - 1), element)
		else:
			self.elements.append(element)
	
	def display(self):
		if self.header is not None:
			print(self.header["text"] + "\n")
		
		for element in self.elements:
			element.display()


class Page:
	def __init__(self):
		self.elements: list = []
		pass
	
	def add(self, element, order = None):
		if order is not None:
			self.elements.insert((order - 1), element)
		else:
			self.elements.append(element)
	
	def display(self):
		for element in self.elements:
			element.display()
