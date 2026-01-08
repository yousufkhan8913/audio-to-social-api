from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/upload", methods=["POST"])
def upload():
    audio = request.files["audio"]
    audio.save("audio.mp3")

    transcript = "Demo transcript (Whisper পরে যোগ হবে)"

    prompt = f"""
    Transcript:
    {transcript}

    Generate:
    - YouTube Title
    - Thumbnail Text
    - Description
    - Facebook Caption
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "transcript": transcript,
        "content": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

