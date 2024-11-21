from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

themes = {
    "love": ["heart", "forever", "romance", "dreams", "you"],
    "sad": ["tears", "broken", "lonely", "pain", "goodbye"],
    "happy": ["smiles", "joy", "sunshine", "beautiful", "laughter"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_lyrics():
    theme = request.form.get('theme', 'love').lower()
    lines = []

    if theme in themes:
        for _ in range(4):  # Generate 4 lines
            lines.append(" ".join(random.sample(themes[theme], 3)))
    else:
        lines.append("Sorry, no lyrics available for this theme.")

    return jsonify({"lyrics": "\n".join(lines)})

if __name__ == "__main__":
    app.run(debug=True)
