from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello Python3 Home!</h1>"

@app.route("/about")

def About():
    return "<h1>Hello Python3 About Page!</h1>"

if __name__ == "__main__":
    app.run(debug=True)