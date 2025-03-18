# flask
A flask learning github repository

##set up
*python -m venv .venv
*pip install flask

##libraries : flask(for flask library) | request (for url ) | make_response (for getting response from url)
             render_templates (used to include html files) | url_for (to redirect) | pandas (for data analysis)

##dynamic routing
*@app.route('/greet/<name>'): use <>(URL processor) to add values dynamically to website
*@app.route('add/<int:num1>/<int:num2>') : can declare variable type
*@app.route('/handle_url_params')
*greeting=request.args.get('greeting'): create input for url to have parameter for greeting

##render_templates
*return render_template('index.html',val=val) : display index.html by passing val to it

##filter
*{{note|upper}} : | is used for filters
*@app.template_filter('reverse_string') : used to create manual filters

##forms
*@app.route('/', methods=['GET','POST']) : used for accessing both get and post methods
*username = request.form.get('username') : used to get form data from html file
*if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username') : for 'GET' it returns index.html and for 'POST' it returns form data

##file-upload
*<form method="POST" action="{{url_for('file_upload')}}" enctype="multipart/form-data">: in html include enctype for uploading files
*<input type="file" name="file" accept="text/plain" required="required">: in html to include file type
*file = request.files['file'] : in python used for accessing uploaded file
*if file.content_type == 'text/plain':
    return file.read().decode() : displays the text in file in html webpage
*file.content_type == 'application/vnd.ms-excel':
        dataframes = pd.read_excel(file) : reads excel data 
        return dataframes.to_html() : displays data in excel format to webpage using pandas

##file download
*file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition':'attachent; filename=result.csv'
        }
    ) : used to download file and convert it to csv format


