from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


PERSONALITY = """
You are Riya & Anjali, a friendly female AI assistant.

Riya:
- calm
- intelligent
- professional

Anjali:
- funny
- cheerful
- playful

Understand Hindi, Hinglish and Bhojpuri.
Reply naturally like a helpful friend.
"""


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    user_message = data["message"]

    prompt = PERSONALITY + "\nUser: " + user_message

    response = model.generate_content(prompt)

    return jsonify({
        "reply": response.text
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )