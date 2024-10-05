
from googletrans import Translator

def translate_text(text, lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation.text

def chatbot_response(user_input, lang):
    # Translate the user input
    translation = translate_text(user_input, lang)
    
    # Return the response
    return translation

# app.py
from flask import Flask, render_template, request
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    user_input = request.form["user_input"]
    lang = request.form["lang"]
    response = chatbot_response(user_input, lang)
    return response

if __name__ == "__main__":
    app.run(debug=True)
