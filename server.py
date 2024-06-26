from flask import Flask, render_template, session, request, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize an empty list to store scores
scores = []

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

@app.route('/duration-and-symbols-pg2')
def duration_and_symbols2():
    return render_template('duration-and-symbols-pg2.html')

@app.route('/duration-and-symbols-pg3')
def duration_and_symbols3():
    return render_template('duration-and-symbols-pg3.html')

# Subdividing page route
@app.route('/subdividing')
def subdividing():
    return render_template('subdividing.html')

@app.route('/subdividing-pg2')
def subdividing_pg2():
    return render_template('subdividing-pg2.html')

@app.route('/timesignature')
def timesignature():
    return render_template('timesignature.html')

@app.route('/timesignature-pg2')
def timesignature_pg2():
    return render_template('timesignature-pg2.html')

@app.route('/timesignature-pg3')
def timesignature_pg3():
    return render_template('timesignature-pg3.html')

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

@app.route('/increment-score2', methods=['POST'])
def increment_score2():
    if 'score' in session:
        session['score'] += 3
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
    
@app.route('/previous-scores', methods=['GET'])
def get_previous_scores():
    # Return the list of previous scores
    return jsonify(scores)

@app.route('/update-scores', methods=['POST'])
def update_scores():
    try:
        # Add the current score to the scores list along with the current date
        if 'score' in session:
            scores.append({'score': session['score']})
            # Clear the session score
            session.pop('score', None)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Score not found in session'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
   app.run(debug=True)