from flask import Flask, request, make_response

app = Flask(__name__)

#index page
@app.route('/')
def index():
    return "<h1>hello world of the hellish</h2>"

#other route contact page
@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return "get request"
    elif request.method == 'POST':
        return "post request"

#dynamic routing
@app.route('/greet/<name>')
def greet(name):
    response = make_response()
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return f"hello {name}"


#declare variable types
@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"{num1}+{num2} = {num1+num2}"

#implicitly add argument names
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.arg.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting}{name}'
    else:
        return "some are missing"

if __name__ == '__main__':
    app.run(debug=True)