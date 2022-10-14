from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'yokeshwaran':'1234','vignesh':'1234','titus':'1234','nithish':'1234'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('resume.html',name=name1)

if __name__ == '__main__':
    app.run()