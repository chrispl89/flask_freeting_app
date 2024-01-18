from flask import Flask, render_template, request, flash

'''
Before start to write the code need to remember about set env in Flask:
set FLASK_APP=app_name.py
set FLASK_ENV=development
'''


app = Flask(__name__)
app.secret_key = 'haselk0!'


@app.route('/hello')
def index():
    flash("What's your name?")
    return render_template('index.html')


@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
