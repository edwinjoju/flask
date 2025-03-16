# flask
A flask learning github repository

#set up
python -m venv .venv
pip install flask

#libraries : flask(for flask library) | request (for url ) | make_response (for getting response from url)
             render_templates (used to include html files) | url_for (to redirect)

#dynamic routing
@app.route('/greet/<name>'): use <>(URL processor) to add values dynamically to website
@app.route('add/<int:num1>/<int:num2>') : can declare variable type
@app.route('/handle_url_params')
greeting=request.args.get('greeting'): create input for url to have parameter for greeting

#render_templates
return render_template('index.html',val=val) : display index.html by passing val to it

#filter
{{note|upper}} : | is used for filters
@app.template_filter('reverse_string') : used to create manual filters



