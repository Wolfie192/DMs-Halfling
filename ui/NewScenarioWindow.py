import FreeSimpleGUI as sg


def build(directories):
	sg.theme("DarkGrey")
	
	window_layout = [
		[select_season_column(directories), select_scenario_column(directories)]
	]
	
	window = sg.Window("New Scenario", window_layout, relative_location = (0, 0), resizable = True, element_padding = 10, margins = (10, 10))
	
	main_loop(window)


def main_loop(window):
	while True:
		event, values = window.read(timeout = 1000)
		if event == sg.WIN_CLOSED:
			break
		
	window.close()

def select_season_column(directories) -> sg.Column:
	layout = [
		[]
	]
	
	return sg.Column(layout, key = "Select Season Column", expand_x = True, expand_y = True)


def select_scenario_column(directories) -> sg.Column:
	layout = [
		[]
	]
	
	return sg.Column(layout, key = "Select Scenario Column", expand_x = True, expand_y = True, visible = False)
