import src.console.console as console
import src.pdf_importer.pdf_extractor as pdf_extractor


def run(directory: dict):
	display()
	main_loop(directory)


def display():
	console.clear()
	print("DM's Halfling - PDF Importer\n\n")
	
	print("Place PDFs to import in the \"Import\" folder.")
	print("PDFs will be deleted from this folder when they are finished being imported.\n\n")
	
	print("[S]tart\n\n")
	
	print("[B]ack | [Q]uit\n\n")


def main_loop(directory: dict):
	while(True):
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
			case "s"|"start":
				pdf_extractor.run(directory)
				display()
