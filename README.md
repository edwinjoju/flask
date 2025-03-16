# flask
A flask learning github repository

#set up
python -m venv .venv
pip install flask

#libraries : flask(for flask library) | request (for url )

#dynamic routing
@app.route('/greet/<name>'): use <>(URL processor) to add values dynamically to website
@app.route('add/<int:num1>/<int:num2>') : can declare variable type
@app.route('/handle_url_params')
greeting=request.args.get('greeting'): create input for url to have parameter for greeting
