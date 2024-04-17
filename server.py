from flask import Flask, render_template, session, request, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'


# ROUTES
@app.route('/')
def home():
    session['score'] = 0
    return render_template('home.html')

# Beat and Tempo page route
@app.route('/beat-and-tempo')
def beat_and_tempo():
    return render_template('beat-and-tempo.html')

@app.route('/common-tempo')
def common():
   return render_template('common-tempo.html')

# Duration and Symbols page route
@app.route('/duration-and-symbols')
def duration_and_symbols():
    return render_template('duration-and-symbols.html')

# Subdividing page route
@app.route('/subdividing')
def subdividing():
    return render_template('subdividing.html')

# Quiz page route
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')
    
@app.route('/score', methods=['GET'])
def get_score():
    if 'score' in session:
        return jsonify({'score': session['score']})
    else:
        return jsonify({'score': 0})
    
@app.route('/increment-score', methods=['POST'])
def increment_score():
    if 'score' in session:
        session['score'] += 1
    else:
        session['score'] = 1
    return jsonify({'success': True})

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Set initial score to 0 if it doesn't exist in session
    if 'score' not in session:
        session['score'] = 0
    return render_template('quiz.html')

# Dynamic route for specific quiz pages like quiz1, quiz2, etc.
@app.route('/quiz<int:quiz_number>', methods=['GET', 'POST'])
def specific_quiz(quiz_number):
    # Construct the template filename based on quiz_number
    quiz_template = f'quiz{quiz_number}.html'
    try:
        return render_template(quiz_template)
    except FileNotFoundError:
        abort(404)  # If the specific quiz template is not found, show a 404 error
	
@app.route('/reset-score', methods=['POST'])
def reset_score():
    if 'score' in session:
        session['score'] = 0
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Score not found in session'})

if __name__ == '__main__':
   app.run(debug=True)
