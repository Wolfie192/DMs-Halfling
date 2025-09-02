from src.pdf_importer.elements import *


class Scenario:
	season: str = None
	scenario: int = None
	tier: str = None
	title: str = None
	author: str = None
	scenario_tags: list[str] = None
	
	def __init__(self, season, scenario, tier = None):
		self.season = season
		self.scenario = scenario
		self.tier = tier
