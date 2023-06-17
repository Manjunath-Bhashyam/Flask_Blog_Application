from flask import Flask,render_template,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'cbe58b2ce8bee23a55ef420f9b5a50b2'

posts = [
    {
        'author':'Dummy 1',
        'title':'Blog_Post 1',
        'content':'First post content',
        'date_posted':'April 15, 2023'
    },
    {
        'author':'Dummy 2',
        'title':'Blog_Post 2',
        'content':'Second post content',
        'date_posted':'April 16, 2023' 
    }
]

@app.route("/")
@app.route("/admin")
def home_page():
    return render_template("homepage.html",posts=posts)

@app.route("/about")
def about_page():
    return render_template("about.html",title = "About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title="Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title="Login", form = form)

if __name__ == "__main__":
    app.run(debug=True)