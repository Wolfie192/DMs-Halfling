class Paragraph:
	def __init__(self, text_list: list[str]):
		self.text: str = ""
		for text in text_list:
			self.text += text
		
		print(self.text)
