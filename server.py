from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    rating = request.form['rating']
    return f"Received: Name: {name}, Email: {email}, Feedback: {feedback}, Rating: {rating}"

if __name__ == '__main__':
    app.run(debug=True)
