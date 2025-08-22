import json
import os
from src.config._directory import DIRECTORY


IMPORTED_MODULES: dict = {
	"Bounties": {},
	"Quests": {},
	"Season 1": {},
	"Season 2": {},
	"Season 3": {},
	"Season 4": {},
	"Season 5": {},
	"Season 6": {},
	"Season 7": {}
}


def setup():
	print("Setting up imported modules dict...")
	for root, _, files in os.walk(DIRECTORY["Modules"]):
		for file in files:
			if file.endswith(".json"):
				with open(os.path.join(root, file), "r") as file:
					data = json.load(file)
					if data["Tier"]:
						IMPORTED_MODULES[data["Season"]][f"{data["Scenario"]} ({data["Tier"]})"] = {"Imported": True}
					else:
						IMPORTED_MODULES[data["Season"]][f"{data["Scenario"]}"] = {"Imported": True}
