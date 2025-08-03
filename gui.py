import FreeSimpleGUI as fsg

import pdf

fsg.theme("DarkGrey15")



def launch_app():
	layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 34], justification = "center", expand_x = True)],
		[fsg.Text("Import PDF", font = ["any", 18], justification = "left")],
		[fsg.In(key = "__PDF_FILE_IMPORT__")],
		[fsg.FileBrowse(target="__PDF_FILE_IMPORT__", file_types = (("PDF Files", "*.pdf"), )), fsg.Button("Import", key = "__IMPORT_SELECTED_PDF__")]
	]
	
	window = fsg.Window("Pathfinder Society Assistant", layout, location=(0,0), size=(800,600), element_padding=2, resizable=True)
	
	while True:
		event, values = window.read()
		if event == fsg.WIN_CLOSED or event== "Cancel":
			break
		elif event == "__IMPORT_SELECTED_PDF__":
			pdf.extract_file(values["__PDF_FILE_IMPORT__"])
		
	close_window(window)

def close_window(window):
	window.close()

if __name__ == "__main__":
	launch_app()
