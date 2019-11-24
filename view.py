from app import app
from flask import render_template

@app.route('/') #  {url:index}
def index():
    name = 'Ivan'
    return render_template('index.html', name=name)
