import os
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        user_input = request.form["tweet"]

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "Analyze the sentiment of the following tweet and classify it as POSITIVE, NEGATIVE, or NEUTRAL: " + user_input,
                    ],
                }
            ]
        )

        response = chat_session.send_message(user_input)
        sentiment = response.text.strip()

    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

