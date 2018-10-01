from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '20ebda5dea90a24375719c286881ea98'

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
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'Success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'c.weihon@gmail.com' and form.password.data == '123':
            flash('Welcome '+form.email.data, 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid login!', 'danger')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    app.run(debug=True)