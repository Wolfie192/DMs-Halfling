import unittest

from tools.scenario_title import parse_scenario_title


class ParseScenarioTitleTests(unittest.TestCase):
    def test_regular_season_title(self):
        self.assertEqual(parse_scenario_title("prefix0107"), ("Season 1", "Scenario 7", 7))

    def test_special_season_title(self):
        self.assertEqual(parse_scenario_title("XXXXX0607"), ("Season 6", "Scenario 7", 7))

    def test_quest_title_with_two_digit_code(self):
        self.assertEqual(parse_scenario_title("XXXXXQ0012"), ("Quests", "Quest 12", 12))

    def test_quest_title_with_one_zero_code(self):
        self.assertEqual(parse_scenario_title("XXXXXQ0123"), ("Quests", "Quest 12", 12))

    def test_bounty_title(self):
        self.assertEqual(parse_scenario_title("XXXXXBty07"), ("Bounties", "Bounty 7", 7))

    def test_missing_or_malformed_title_is_rejected(self):
        for title in (None, "", "prefixABCD"):
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    parse_scenario_title(title)


if __name__ == "__main__":
    unittest.main()
