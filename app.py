from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/teams')
def teams():
    return render_template('teams.html')


@app.route('/uml')
def uml():
    return render_template('uml.html')