import sys

def store_scores(length: int, arguments: list) -> list:
    scores = []
    i = 0
    while i < length:
        try:
            score = int(arguments[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid score: {arguments[i]}")
        i += 1
    return scores

def ft_score_analytics(scores: list):

    if not scores:
        print("No valid scores to analyze.")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    highest_score = max(scores)
    lowest_score = min(scores)
    score_range = highest_score - lowest_score

    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {score_range}")

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = store_scores(len(sys.argv) - 1, sys.argv[1:])
        print(f"Scores processed: {scores}")
        ft_score_analytics(scores)
