from flask import Flask, jsonify

app = Flask(__name__)

# In-memory vote store: {candidate_name: vote_count}
votes = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the App"


@app.route("/health", methods=["GET"])
def health():
    return "App is running"


@app.route("/vote/<name>", methods=["GET"])
def vote(name):
    candidate = name.strip().lower()
    votes[candidate] = votes.get(candidate, 0) + 1
    return jsonify(
        {
            "message": f"Vote recorded for {candidate}",
            "candidate": candidate,
            "votes": votes[candidate],
        }
    )


@app.route("/results", methods=["GET"])
def results():
    return jsonify(votes)


@app.route("/reset", methods=["POST", "GET"])
def reset_votes():
    votes.clear()
    return jsonify({"message": "All votes reset successfully"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
