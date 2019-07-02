from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

# replace with your own postgres
# DB_URL = 'postgresql://postgres:Brian8053@@127.0.0.1:5432/mailingApp'

# heroku 
DB_URL = 'postgres://mslemiksoajbnk:1e7fa29efc4ee02ea46586fa6784da17d77ed9f08f2186f0a59fe01b64821b92@ec2-174-129-227-146.compute-1.amazonaws.com:5432/d1uhbdtngmk28p'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='some-secret-string'

db = SQLAlchemy(app)

from signupmodel import Signupmodel

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        try:
            # getting the values from the inputs in the form
            fullname = request.form['fullName']
            dob = request.form['dob']
            gender = request.form['gender']
            email = request.form['email']
            phone = request.form['phone']

            # before we add a user, we first check if the username exists
            if Signupmodel.check_email_exists(email=email):
                flash('Email already in use!','danger')
                return redirect(url_for('register'))
            else:
                # add the user to be the DB
                user = Signupmodel(fullName=fullname,dob=dob,gender=gender,email=email,phone=phone)
                user.create_user()
                flash('Account successfully created','success')
                return redirect(url_for('register'))
        except Exception as e:
            print(e)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)    