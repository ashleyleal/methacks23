from flask import Flask, render_template, url_for, request, jsonify
import cohere
import cohereIntegration

app = Flask(__name__) 

#app decorator that creates a default route for program; defined in function
@app.route('/')
def index():
    return "Hello World"  

if __name__ == "__main__":
    app.run(debug=True)











