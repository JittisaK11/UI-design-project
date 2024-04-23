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

<<<<<<<<< Temporary merge branch 1
@app.route('/quiz<int:id>', methods=['GET', 'POST'])
def quiz_id(id):
    # Constructs the filename based on the quiz ID
    quiz_file = f'quiz{id}.html'
    return render_template(quiz_file)

# Function to reset the score to 0
@app.route('/reset_score', methods=['POST'])
def reset_score():
    session['score'] = 0
    return jsonify({'message': 'Score reset successfully'})

# Function to add 1 point to the score
@app.route('/add_point', methods=['POST'])
def add_point():
    session['score'] += 1
    return jsonify({'message': 'Point added successfully'})
=========
@app.route('/common-tempo')
def common():
    return render_template('common-tempo.html')
 
>>>>>>>>> Temporary merge branch 2

if __name__ == '__main__':
   app.run(debug=True)
