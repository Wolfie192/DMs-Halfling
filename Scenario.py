import os

import pdf


def get_image_dict(img_dir, season: int, scenario: int) -> dict:
	image_dict = {}
	match season:
		case 1:
			match scenario:
				case 1:
					image_dict["Where On Golarion"] = os.path.join(img_dir, "extracted_image_page3_img1.jpeg")
					image_dict["Janira Gavix"] = os.path.join(img_dir, "extracted_image_page42_img1.png")
					image_dict["Calisro Benarry"] = os.path.join(img_dir, "extracted_image_page43_img1.jpeg")
					image_dict["Eando Kline"] = os.path.join(img_dir, "extracted_image_page44_img1.jpeg")
					image_dict["Fola Barun"] = os.path.join(img_dir, "extracted_image_page45_img1.jpeg")
					image_dict["Gorm Greathammer"] = os.path.join(img_dir, "extracted_image_page46_img1.jpeg")
					image_dict["Aaqir Al-Hakam"] = os.path.join(img_dir, "extracted_image_page47_img1.png")
					image_dict["Ambrus Valsin"] = os.path.join(img_dir, "extracted_image_page48_img1.png")
					image_dict["Gloriana Morilla"] = os.path.join(img_dir, "extracted_image_page49_img1.jpeg")
					image_dict["Kreighton Shane"] = os.path.join(img_dir, "extracted_image_page50_img1.jpeg")
					image_dict["Sorrina Westyr"] = os.path.join(img_dir, "extracted_image_page51_img1.jpeg")
					image_dict["Tamrin Credence"] = os.path.join(img_dir, "extracted_image_page52_img1.jpeg")
					image_dict["Urwal"] = os.path.join(img_dir, "extracted_image_page53_img1.jpeg")
					image_dict["Valais Durant"] = os.path.join(img_dir, "extracted_image_page54_img1.jpeg")
					image_dict["Zarta Dralneen"] = os.path.join(img_dir, "extracted_image_page55_img1.png")
					image_dict["Fleshforge Creature"] = os.path.join(img_dir, "extracted_image_page56_img1.jpeg")
					image_dict["Tavvar Hamavsi"] = os.path.join(img_dir, "extracted_image_page57_img1.png")
					image_dict["Zombie"] = os.path.join(img_dir, "extracted_image_page58_img1.jpeg")
					image_dict["Zombie Brute"] = os.path.join(img_dir, "extracted_image_page59_img1.jpeg")
					image_dict["Cacodaemon"] = os.path.join(img_dir, "extracted_image_page60_img1.jpeg")
					image_dict["Ceustodaemon"] = os.path.join(img_dir, "extracted_image_page61_img1.jpeg")
					image_dict["Goblin Commando"] = os.path.join(img_dir, "extracted_image_page62_img1.jpeg")
					image_dict["Goblin Warrior"] = os.path.join(img_dir, "extracted_image_page62_img1.jpeg")
					image_dict["Goblin Pyro"] = os.path.join(img_dir, "extracted_image_page63_img1.jpeg")
					image_dict["Petrified Pathfinder"] = os.path.join(img_dir, "extracted_image_page64_img1.png")
	
	return image_dict


def treasure_table(season: int, scenario: int) -> dict:
	gold_per_bundle: dict = {}
	
	match season:
		case 1:
			match scenario:
				case 1:
					gold_per_bundle[1] = 1.4
					gold_per_bundle[2] = 2.2
					gold_per_bundle[3] = 3.8
					gold_per_bundle[4] = 6.4
	
	return gold_per_bundle


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


class Scenario:
	def __init__(self, bin_dir, season, scenario):
		self.season: int = int(season)
		self.scenario: int = int(scenario)
		self.root_dir = os.path.join(bin_dir, f"S{season}S{scenario}")
		self.asset_dir = os.path.join(self.root_dir, "Assets")
		self.img_dir = os.path.join(self.asset_dir, "Images")
		self.image_dict: dict = get_image_dict(self.img_dir, season, scenario)
		self.challenge_points: int = 0
		self.treasure_bundles_found: int = 0
		self.gold_per_bundle: dict = treasure_table(self.season, self.scenario)
		self.event_reporting_sheet: dict = event_reporting_sheet(self.season, self.scenario)
