from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        translator = Translator()
        marathi_text = request.form['marathi_text']
        translated = translator.translate(marathi_text, src='mr', dest='hi')
        hindi_text = translated.text
        return render_template('translate.html', marathi_text=marathi_text, hindi_text=hindi_text)

if __name__ == '__main__':
    app.run(debug=True)
