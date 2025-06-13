from flask import Flask, request, jsonify
from flask_cors import CORS
from model import train_model, predict_match
from simulate_bracket import simulate_tournament

app = Flask(__name__)
CORS(app)

model = train_model()

@app.route("/predict_match", methods=["POST"])
def predict():
    data = request.json
    team1_elo = data.get("team1_elo")
    team2_elo = data.get("team2_elo")
    winner = predict_match(model, team1_elo, team2_elo)
    return jsonify({"winner": winner})

@app.route("/simulate_bracket", methods=["POST"])
def simulate():
    final_winner, results = simulate_tournament()
    return jsonify({"final_winner": final_winner, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
