class Scenario:
	def __init__(self, root_dir, asset_dir, image_dir, file_input,
	             author, title, tier_min, tier_max, scenario_tags):
		self.root_dir = root_dir
		self.asset_dir = asset_dir
		self.image_dir = image_dir
		self.file_input = file_input
		self.author = author
		self.title = title
		self.tier_min = tier_min
		self.tier_max = tier_max
		self.scenario_tags = scenario_tags
		self.players: dict = {}
		self.challenge_points: int = 0
	
	def add_player(self, player_name, character_name, character_level):
		self.players[player_name] = {
			"Character Name": character_name,
			"Level": character_level
		}
		
		self.update_challenge_points()

	def update_challenge_points(self):
		self.challenge_points = 0
		
		for key in self.players.keys():
			level = self.players[key]["Level"]
			if level == self.tier_min:
				self.challenge_points += 2
			if level == (self.tier_min + 1):
				self.challenge_points += 3
			if level == (self.tier_max - 1):
				self.challenge_points += 4
			if level == self.tier_max:
				self.challenge_points += 6


if __name__ == "__main__":
	pass
