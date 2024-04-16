from flask import Flask, render_template, session, request, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'


# ROUTES
@app.route('/')
def home():
    return render_template('home.html')

# Beat and Tempo page route
@app.route('/beat-and-tempo')
def beat_and_tempo():
    return render_template('beat-and-tempo.html')

# Duration and Symbols page route
@app.route('/duration-and-symbols')
def duration_and_symbols():
    return render_template('duration-and-symbols.html')

# Subdividing page route
@app.route('/subdividing')
def subdividing():
    return render_template('subdividing.html')

# Quiz page route
@app.route('/quiz')
@app.route('/', methods=['GET', 'POST'])
def main():
    # Set initial score to 0 if it doesn't exist in session
    if 'score' not in session:
        session['score'] = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')

<<<<<<< HEAD
@app.route('/common-tempo')
def common():
    return render_template('common-tempo.html')
 
=======
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
>>>>>>> ee61b7bba4662599b6bcd6c8a3aaec36b8604e44

if __name__ == '__main__':
   app.run(debug=True)
