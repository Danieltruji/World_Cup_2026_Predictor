import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # Dummy model setup for now — replace with real logic later
    df = pd.DataFrame({
        "home_team_elo": [2000, 1950, 1900],
        "away_team_elo": [1900, 1800, 1850],
        "outcome": [1, 1, 0]  # 1 = home win, 0 = away win
    })

    df["elo_diff"] = df["home_team_elo"] - df["away_team_elo"]
    X = df[["elo_diff"]]
    y = df["outcome"]

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def predict_match(model, team1_elo, team2_elo):
    elo_diff = team1_elo - team2_elo
    prediction = model.predict([[elo_diff]])
    return "team1" if prediction[0] == 1 else "team2"
