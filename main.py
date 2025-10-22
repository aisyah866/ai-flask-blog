from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # izinkan akses dari blog

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"result": "Tolong masukkan pertanyaan!"})

    try:
        return jsonify({"result": f"Pesan kamu diterima: {prompt}"})
    except Exception as e:
        return jsonify({"result": f"Terjadi kesalahan: {str(e)}"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
