from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    val = "Larcade"
    power_level=300
    attributes = ['fire','water','lightning','earth','light','dark']
    return render_template('index.html',val=val,power_level=power_level,attr=attributes)

@app.route('/about')
def about():
    note = "this is a roberry"
    return render_template('index.html',note=note)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=5):
    return s *times

if __name__ == '__main__':
    app.run(debug=True)