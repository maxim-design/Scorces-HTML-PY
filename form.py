from Data import Players_Data
from flask import Flask, render_template, request, jsonify, redirect
import os, json


TEMPLATE_DIR = os.path.abspath('./Data/FormTemplates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    score = request.form['score']
    if name and score:
        
        Players_Data.apply_current_score_to_player(name, int(score))
        
        return redirect('/') #jsonify(success=True)
    else:
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True, port=23789)
