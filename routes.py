from flask import Flask
from flask import render_template
from flask import url_for, redirect

options = {'Home' : 'home', 'About' : 'about', 'Projects' : 'projects'}

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('home.html', options=options)

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/projects')
def projects():

    projects_dict = {}

    with open('projects.txt', 'r') as file:

        for line in file:

            curr_project = line.strip('\n').split('@')
            projects_dict[curr_project[0]] = [curr_project[1], curr_project[2]]

    return render_template('projects.html', projects_dict=projects_dict)

@app.route('/github')
def github():

    return redirect('https://github.com/Cpreister109')

@app.errorhandler(404)
def not_found(e):

    return render_template('404.html'), 400

@app.errorhandler(500)
def internal_error(e):

    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()