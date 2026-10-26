from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "cloud-deployment-capstone",
        "message": "Automated Cloud Deployment Pipeline",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloud-deployment-capstone"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
