from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Chong Wei Hon',
        'title': 'Blog Post 1',
        'content': '1st Post Content',
        'date_posted': 'Sept 28, 2018'
    },
    {
        'author': 'Wong Fun Ying',
        'title': 'Blog Post 2',
        'content': '2nd Post Content',
        'date_posted': 'Aug 28, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Main')

@app.route("/about")
def About():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)