# simulate_bracket.py

from model import predict_match, train_model

def simulate_tournament():
    model = train_model()
    
    # Dummy bracket — replace with actual team data later
    matches = [
        {"team1": "Brazil", "team1_elo": 2000, "team2": "Germany", "team2_elo": 1950},
        {"team1": "France", "team1_elo": 1980, "team2": "Argentina", "team2_elo": 2020}
    ]

    results = []
    for match in matches:
        winner_key = predict_match(model, match["team1_elo"], match["team2_elo"])
        winner = match["team1"] if winner_key == "team1" else match["team2"]
        results.append({
            "match": f"{match['team1']} vs {match['team2']}",
            "winner": winner
        })

    # Pick a dummy final winner for now
    final_winner = results[0]["winner"]
    return final_winner, results
