from flask import Flask, render_template, url_for, request, jsonify
import cohere
import cohereIntegration
import subprocess

app = Flask(__name__, template_folder='static/templates') 

#app decorator that creates a default route for program; defined in function
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process-user-input", methods=["POST"])
def process_user_input():
    user_input_value = request.json.get("userInputValue")
    # Process the user input in the Flask server
    # Example: Call the cohere API or perform other operations
    # Use the user_input_value as needed

    # Pass the userInputValue to the happy.py script as a command-line argument
    subprocess.run(["python", "CohereIntegration.py", user_input_value])

    return "User input processed successfully"

if __name__ == "__main__":
    app.run(debug=True)











