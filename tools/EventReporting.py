def event_reporting_sheet(season: int, scenario: int) -> dict:
	event_reporting_sheet_dict: dict = {}
	
	match season:
		case 1:
			match scenario:
				case 1:
					event_reporting_sheet_dict = {
							"Date": None,
							"Event Code": None,
							"Location": None,
							"GM Org Play #": None,
							"GM Name": None,
							"GM Faction": None,
							"Adventure #": None,
							"Adventure Name": None,
							"Reporting Codes": {
								"A": False,
								"B": False,
								"C": False,
								"D": False,
								"N/A": False,
							},
							"Bonus Faction Goal Achieved": {
								"Yes": False,
								"No": False,
								"N/A": False
							},
							"Scenario-Based Infamy Earned": {
								"Yes": False,
								"No": False,
								"N/A": False
							},
							"Fame Earned": None,
							"Player 1": {
								"Player Name": None,
								"Class": None,
								"Character Name": None,
								"Org Play #": None,
								"Level": None,
								"Faction": {
									"Envoy's Alliance": False,
									"Grand Archive": False,
									"Horizon Hunters": False,
									"Radiant Oath": False,
									"Verdant Wheel": False,
									"Vigilant Seal": False
								},
								"Slow Track": False,
								"Dead": False,
								"Infamy": False
							},
						"Player 2": {
							"Player Name": None,
							"Class": None,
							"Character Name": None,
							"Org Play #": None,
							"Level": None,
							"Faction": {
								"Envoy's Alliance": False,
								"Grand Archive": False,
								"Horizon Hunters": False,
								"Radiant Oath": False,
								"Verdant Wheel": False,
								"Vigilant Seal": False
							},
							"Slow Track": False,
							"Dead": False,
							"Infamy": False		
							},
						"Player 3": {
							"Player Name": None,
							"Class": None,
							"Character Name": None,
							"Org Play #": None,
							"Level": None,
							"Faction": {
								"Envoy's Alliance": False,
								"Grand Archive": False,
								"Horizon Hunters": False,
								"Radiant Oath": False,
								"Verdant Wheel": False,
								"Vigilant Seal": False
							},
							"Slow Track": False,
							"Dead": False,
							"Infamy": False		
							},		
						"Player 4": {
							"Player Name": None,
							"Class": None,
							"Character Name": None,
							"Org Play #": None,
							"Level": None,
							"Faction": {
								"Envoy's Alliance": False,
								"Grand Archive": False,
								"Horizon Hunters": False,
								"Radiant Oath": False,
								"Verdant Wheel": False,
								"Vigilant Seal": False
							},
							"Slow Track": False,
							"Dead": False,
							"Infamy": False		
							},
						"Player 5": {
							"Player Name": None,
							"Class": None,
							"Character Name": None,
							"Org Play #": None,
							"Level": None,
							"Faction": {
								"Envoy's Alliance": False,
								"Grand Archive": False,
								"Horizon Hunters": False,
								"Radiant Oath": False,
								"Verdant Wheel": False,
								"Vigilant Seal": False
							},
							"Slow Track": False,
							"Dead": False,
							"Infamy": False		
							},
						"Player 6": {
							"Player Name": None,
							"Class": None,
							"Character Name": None,
							"Org Play #": None,
							"Level": None,
							"Faction": {
								"Envoy's Alliance": False,
								"Grand Archive": False,
								"Horizon Hunters": False,
								"Radiant Oath": False,
								"Verdant Wheel": False,
								"Vigilant Seal": False
							},
							"Slow Track": False,
							"Dead": False,
							"Infamy": False		
							},
						}
	
	return event_reporting_sheet_dict
