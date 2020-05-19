import sys
import spacy
from flask import Flask, render_template, redirect, url_for, request
from flask_debug import Debug


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("page.html")

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method =='POST':
        nlp = spacy.load("en_core_web_sm")
        input = request.form['script']
        k = nlp(input)
        lst = []
        for token in k:
            ele = (f'{token.text:{10}}{token.pos_:{10}}{spacy.explain(token.tag_):{10}}')
            lst.append(ele)

        return render_template("output.html", len= len(lst), lst = lst)
        
        


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True )
    
