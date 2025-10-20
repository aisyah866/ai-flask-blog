from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(api_key="API_KEY_KAMU")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"result": "Tolong masukkan pertanyaan!"})

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({"result": response.text})
    except Exception as e:
        return jsonify({"result": f"Terjadi kesalahan: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)