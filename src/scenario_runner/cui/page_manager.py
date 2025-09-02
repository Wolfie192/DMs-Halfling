from src.console import console


def run(selected_scenario_path):
	_display()
	_main_loop(selected_scenario_path)


def _display():
	console.clear()
	print(f"DM's Halfling - Scenario Runner\n\n")
	
	print()
	
	print("[B]ack | [Q]uit")


def _main_loop(selected_scenario_path):
	while(True):
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
			case _:
				_display()
