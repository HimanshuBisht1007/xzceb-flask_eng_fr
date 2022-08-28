from machinetranslation import translator
from flask import Flask, render_template, request
import machinetranslation
import json

app = Flask("Web Translator", template_folder="./templates")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = machinetranslation.translator.englishtofrench(textToTranslate)
    return result

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = machinetranslation.translator.frenchtoenglish(textToTranslate)
    return result

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
