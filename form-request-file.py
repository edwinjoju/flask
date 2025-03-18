from flask import Flask, render_template, request, Response, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'edwinjoju' and password==12345678:
        return "Success"
    else:
        return "Failed"
    
@app.route('/file_upload', methods=['GET','POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.ms-excel':
        dataframes = pd.read_excel(file)
        return dataframes.to_html()
    
@app.route('/convert_csv',methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition':'attachent; filename=result.csv'
        }
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)