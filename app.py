from flask import Flask, request, jsonify

app = Flask(__name__)
current_url = None

@app.route("/update-url", methods=["POST"])
def update_url():
    global current_url
    data = request.get_json()
    current_url = data.get("url")
    return jsonify({"message": "URL mise à jour", "url": current_url})

@app.route("/get-url", methods=["GET"])
def get_url():
    if current_url:
        return jsonify({"url": current_url})
    else:
        return jsonify({"error": "Aucune URL disponible"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
