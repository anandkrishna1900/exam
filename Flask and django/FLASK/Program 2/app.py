from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)  # integrate Bootstrap with the app

@app.route('/')
def index():
    # pass data to the template
    courses = ['Python', 'Flask', 'Django']
    return render_template('index.html', user='Roshan', items=courses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
