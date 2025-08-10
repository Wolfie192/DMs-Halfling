import os


def get_scenario_tags(file_input, season: str, scenario: str) -> list[str]:
	tag_list: list[str] = []
	
	match int(season):
		case 1:
			match int(scenario):
				case 7:
					tag_list = [file_input[32]]
			
	return tag_list


def setup_new_session(bin_dir, season: str, scenario: str):
	output_dir = os.path.join(bin_dir, f"S{season}S{scenario}")
	extracted_text_path = os.path.join(output_dir, "extracted_text.txt")
	asset_dir = os.path.join(output_dir, "Assets")
	image_dir = os.path.join(asset_dir, "Images")
	file_input: list[str] = []
	content: dict = {}
	
	with open(extracted_text_path, "r", encoding = "utf-8") as f:
		lines = f.readlines()
		for line in lines:
			file_input.append(line.replace("\n", ""))
	
	author: str = file_input[8][3:]
	title: str = file_input[9]
	tier: str = file_input[11].replace("TIER ", "")
	tier_min: int = int(tier.split("–")[0])
	tier_max: int = int(tier.split("–")[1])
	scenario_tags: list[str] = get_scenario_tags(file_input, season, scenario)
	

if __name__ == "__main__":
	bin_dir = os.path.abspath("../bin")
	setup_new_session(bin_dir, "01", "07")
