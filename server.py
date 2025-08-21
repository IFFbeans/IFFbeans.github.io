from flask import Flask, request, jsonify
import openai
import os

app = Flask(_name_)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/generate-story", methods=["POST"])
def generate_story():
    data = request.json
    prompt = data.get("prompt", "")
    full_prompt = f"Write a short, fun, kid-friendly story based on: {prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": full_prompt}]
    )

    story = response.choices[0].message.content
    return jsonify({"story": story})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=3000)
