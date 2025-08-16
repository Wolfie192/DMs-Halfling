import json
import os

import FreeSimpleGUI as sg
import tools.formatter as elements


def build(season, scenario):
	print(season, scenario)
	bin_dir = os.path.abspath("../bin")
	modules_dir = os.path.join(bin_dir, "Modules")
	season_dir = os.path.join(modules_dir, season)
	scenario_dir = os.path.join(season_dir, f"Scenario {scenario}")
	#! This is giving me a "no such file or directory" error and not sure why. Need to look into.
	file_path = os.path.join(scenario_dir, "output.json")

	window_layout = [
		[elements.Paragraph(file_path, [("2.12.1", "2.12.8")]).compose()]
	]
	
	window = sg.Window(f"DM's Halfling Assistant", window_layout, relative_location = (0, 0), resizable =  True, element_padding = 10, margins = (10, 10))
	
	main_loop(window)


def main_loop(window):
	while True:
		event, values = window.read(timeout = 1000)
		if event == sg.WIN_CLOSED:
			break
	
	window.close()
