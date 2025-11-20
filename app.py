from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///colchester.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey123'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    marketing_opt_in = db.Column(db.Boolean, default=False)

    comments = db.relationship('Comment', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    comments = db.relationship('Comment', backref='place', lazy=True)
    likes = db.relationship('Like', backref='place', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/logreg')
def logreg():
    return render_template('logreg.html')

@app.route('/success')
def success():
    return render_template('success.html')

# This is just a simple page which shows how to get data onto your web pages, making it a data-driven website
@app.route('/data')
def data():
    users = User.query.all()
    places = Place.query.all()
    comments = Comment.query.all()
    likes = Like.query.all()
    return render_template('data.html',
                           users=users,
                           places=places,
                           comments=comments,
                           likes=likes)

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(username=name).first()

    if not user:
        return "User not found!", 400

    if user.password != password:
        return "Wrong password!", 400

    # Save user login status
    session['user_id'] = user.id
    session['username'] = user.username

    return redirect('/')   # Redirect to homepage

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




@app.route('/uploadContact', methods=['POST'])
def upload_contact():
    name = request.form.get('name')
    password = request.form.get('password')
    marketing = 'marketing_opt_in' in request.form  # Checkbox returns True if checked

    # Basic validation
    # Required fields
    if not name or not password:
        return "Name and password are required!", 400

    # Check if username already exists (the simple unique check)
    existing_user = User.query.filter_by(username=name).first()
    if existing_user:
        return "Username already exists. Please choose another.", 400

    # Length validation (backup to JS)
    if 5 > len(name) > 25 or 5 > len(password) > 25:
        return "Username or password must between 5-25 characters!", 400

    # Save to database
    new_user = User(username=name, password=password, marketing_opt_in=marketing)
    db.session.add(new_user)
    db.session.commit()

    return render_template("success.html", name=name)



if __name__ == '__main__':
    app.run(debug=True)