import os


DIRECTORY: dict = {}


def make_directory(dir_path):
	if not os.path.exists(dir_path):
		os.mkdir(dir_path)


def setup():
	print("Setting up directory...")
	if os.path.exists("./bin"):
		bin_dir = os.path.abspath("./bin")
	if os.path.exists("../bin"):
		bin_dir = os.path.abspath("../bin")
	else:
		bin_dir = os.path.abspath("../bin")
	make_directory(bin_dir)
	
	configs_dir = os.path.join(bin_dir, "Configs")
	make_directory(configs_dir)
	modules_dir = os.path.join(bin_dir, "Modules")
	make_directory(modules_dir)
	saves_dir = os.path.join(bin_dir, "Saves")
	make_directory(saves_dir)
	bounties_dir = os.path.join(modules_dir, "Bounties")
	make_directory(bounties_dir)
	quests_dir = os.path.join(modules_dir, "Quests")
	make_directory(quests_dir)
	season1_dir = os.path.join(modules_dir, "Season 1")
	make_directory(season1_dir)
	season2_dir = os.path.join(modules_dir, "Season 2")
	make_directory(season2_dir)
	season3_dir = os.path.join(modules_dir, "Season 3")
	make_directory(season3_dir)
	season4_dir = os.path.join(modules_dir, "Season 4")
	make_directory(season4_dir)
	season5_dir = os.path.join(modules_dir, "Season 5")
	make_directory(season5_dir)
	season6_dir = os.path.join(modules_dir, "Season 6")
	make_directory(season6_dir)
	season7_dir = os.path.join(modules_dir, "Season 7")
	make_directory(season7_dir)
	
	
	DIRECTORY["bin"] = bin_dir
	DIRECTORY["Configs"] = configs_dir
	DIRECTORY["Modules"] = modules_dir
	DIRECTORY["Saves"] = saves_dir
	DIRECTORY["Bounties"] = bounties_dir
	DIRECTORY["Quests"] = quests_dir
	DIRECTORY["Season 1"] = season1_dir
	DIRECTORY["Season 2"] = season2_dir
	DIRECTORY["Season 3"] = season3_dir
	DIRECTORY["Season 4"] = season4_dir
	DIRECTORY["Season 5"] = season5_dir
	DIRECTORY["Season 6"] = season6_dir
	DIRECTORY["Season 7"] = season7_dir
	
