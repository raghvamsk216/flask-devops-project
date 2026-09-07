from flask import Flask

# Initialize the Flask application instance
app = Flask(__name__)

# Define a route for the home/root URL page
@app.route("/")
def home():
    return "<h1>Devops Project is sucessfully deployed.</h1>"

# Run the app locally in debug mode if executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
