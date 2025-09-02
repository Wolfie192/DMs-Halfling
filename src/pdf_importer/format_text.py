from src.pdf_importer.elements import *
from src.pdf_importer.scenario import Scenario
import sys


def formatter(line_dict, scenario_dir) -> Scenario:
	tier = None
	
	scenario_str = scenario_dir.split("\\")[-1]
	if scenario_str.endswith(")"):
		tier = scenario_str.split(" ")[-1]
		scenario = int(scenario_str.split(" ")[-2])
	else:
		scenario = int(scenario_str.split(" ")[-1])
		
	season = scenario_dir.split("\\")[-2]
	
	match season:
		case "Bounties":
			pass
		case "Quests":
			pass
		case "Season 1":
			match scenario:
				case 7:
					return _season_1_scenario_7_formatter(line_dict)
		case "Season 2":
			match scenario:
				case 0:
					match tier:
						case "(3-6)":
							return _season_2_scenario_0_tier_3_to_6_formatter(line_dict)
		case "Season 3":
			pass
		case "Season 4":
			pass
		case "Season 5":
			pass
		case "Season 6":
			pass


def _season_1_scenario_7_formatter(line_dict) -> Scenario:
	module = Scenario(season ="Season 1", scenario = 7)
	module.title = line_dict["2.9.0.0"]["text"]
	module.author = line_dict["1.22.1.0"]["text"]
	module.scenario_tags = [line_dict["1.10.0.0"]["text"]]
	
	page_1 = Page()

	where_on_golarion = Section(header = line_dict["2.17.0.0"])
	paragraph_1 = Paragraph()
	paragraph_1.add_text(line_dict["2.16.0.0"], line_dict["2.16.0.1"], line_dict["2.16.1.0"], line_dict["2.16.2.0"], line_dict["2.16.3.0"], line_dict["2.16.4.0"], line_dict["2.16.5.0"], line_dict["2.16.5.1"], line_dict["2.16.5.2"], line_dict["2.16.6.0"], line_dict["2.16.7.0"], line_dict["2.16.7.1"], line_dict["2.16.7.2"])
	where_on_golarion.add(paragraph_1)
	page_1.add(where_on_golarion)
	
	gm_synopsis = Section()
	paragraph_2 = Paragraph()
	paragraph_2.add_text(line_dict["2.11.0.0"], line_dict["2.11.0.1"], line_dict["2.11.1.0"], line_dict["2.11.2.0"])
	gm_synopsis.add(paragraph_2)
	page_1.add(gm_synopsis)
	
	page_1.display()

	#? This is for testing purposes to prevent the rest of the program from running and overwriting the display to the terminal window.
	sys.exit()
	return module


def _season_2_scenario_0_tier_3_to_6_formatter(line_dict) -> Scenario:
	module = Scenario(season ="Season 2", scenario = 0, tier ="(3-6)")

	return module
