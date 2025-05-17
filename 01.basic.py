from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print ("welcome to Home Page")
    return "Welcome to Home Page"

@app.route("/index")
def index():
    return ("welcome to Index Page")

if __name__ == "__main__":
    app.run(debug=True)




