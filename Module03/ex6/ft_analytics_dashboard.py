
def main() -> None:
    print("=== Game Analytics Dashboard ===")
    print()

    players = ["alice", "bob", "charlie", "diana"]

    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }

    achievements = {
        "alice": {"first_kill": 5, "level_10": 39, "boss_slayer": 9},
        "bob": {"first_kill": 3, "level_10": 3, "boss_slayer": 0},
        "charlie": {"level_10": 25, "treasure_hunter": 7, "boss_slayer": 5},
        "diana": {"first_kill": 2, "level_10": 1, "treasure_hunter": 1},
    }

    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "north",
        "diana": "central",
    }

    print("=== List Comprehension ===")

    high_scorers = []
    for player in players:
        if scores[player] > 2000:
            high_scorers.append(player)

    doubled_scores = []
    for score in scores.values():
        doubled_scores.append(score * 2)

    active_players = []
    for player in players:
        if len(achievements[player]) > 1:
            active_players.append(player)

    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", doubled_scores)
    print("Active players:", active_players)
    print()

    print("=== Dictionary Comprehension ===")

    player_scores = {}
    for player in players:
        player_scores[player] = scores[player]

    achievement_counts = {}
    for player in players:
        achievement_counts[player] = len(achievements[player])

    score_categories = {"high": 0, "medium": 0, "low": 0}
    for score in scores.values():
        if score > 2000:
            score_categories["high"] += 1
        elif 1500 <= score <= 2000:
            score_categories["medium"] += 1
        else:
            score_categories["low"] += 1

    print("Player scores:", player_scores)
    print("Achievement counts:", achievement_counts)
    print("Score categories:", score_categories)
    print()

    print("=== Set Comprehension ===")

    unique_players = set()
    for player in players:
        unique_players.add(player)

    unique_achievements = set()
    for player_list in achievements.values():
        for achievement in player_list:
            if achievement in ["level_10", "first_kill", "boss_slayer"]:
                unique_achievements.add(achievement)

    active_regions = set()
    for region in regions.values():
        if region in ["north", "central"]:
            active_regions.add(region)

    print("Unique players:", unique_players)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", active_regions)
    print()

    print("=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = 0
    total_unique_achievements = 0

    for achievement_dict in achievements.values():
        for achievement in achievement_dict:
            if achievement in ["level_10", "first_kill", "boss_slayer"]:
                total_unique_achievements += achievement_dict[achievement]

    average_score = sum(scores.values()) / len(scores)
    top_player = max(scores, key=scores.get)

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        "Top performer:",
        top_player,
        f"({scores[top_player]} points, "
        f"{achievement_counts[top_player]} achievements)"
    )


if __name__ == "__main__":
    main()
