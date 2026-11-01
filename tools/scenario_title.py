def parse_scenario_title(title: str | None) -> tuple[str, str, int]:
    """Return season label, scenario label, and scenario number from a PDF title."""
    if not title:
        raise ValueError("PDF title is empty.")

    try:
        if title[6:8] in ("60", "61"):
            season = int(title[5:7])
            scenario = int(title[7:9])
        elif title[5:8] == "Q00":
            season = 0
            scenario = int(title[8:10])
        elif title[5:7] == "Q0":
            season = 0
            scenario = int(title[7:9])
        elif title[5] == "B":
            season = 99
            scenario = int(title[8:10].replace("E", ""))
        else:
            season = int(title[6:8])
            scenario = int(title[8:10])
    except (IndexError, ValueError) as error:
        raise ValueError(f"Could not parse season and scenario from PDF title: {title!r}.") from error

    match season:
        case 0:
            return "Quests", f"Quest {scenario}", scenario
        case 99:
            return "Bounties", f"Bounty {scenario}", scenario
        case _:
            return f"Season {season}", f"Scenario {scenario}", scenario
