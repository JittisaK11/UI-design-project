from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

import logging

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def main():
   return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
   return render_template('quiz.html')

@app.route('/duration-and-symbols-1')
def duration_and_symbols():
    return render_template('duration-and-symbols-1.html')

@app.route('/quiz<int:id>', methods=['GET', 'POST'])
def quiz_id(id):
    # Constructs the filename based on the quiz ID
    quiz_file = f'quiz{id}.html'
    return render_template(quiz_file)

if __name__ == '__main__':
   app.run(debug = True)