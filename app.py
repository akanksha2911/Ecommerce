from flask import Flask,render_template,request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
with open('config.json','r') as c:
    params = json.load(c)['params']

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bangleselling'
db = SQLAlchemy(app)

class Newsletter(db.Model):
    #sno,mailId,dateTime
   sno = db.Column(db.Integer,primary_key=True)
   mailId = db.Column(db.String(50),nullable=False)
   #datetime = db.Column(db.string(12),nullable=True) 


@app.route("/",methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        mailId = request.form.get('mailId')
        entry = Newsletter(mailId = mailId)
        db.session.add(entry)
        db.session.commit()
    return render_template("index.html",params = params)

@app.route("/contact")
def contact():
    return render_template("contact.html",params = params)

@app.route("/product")
def product():
    return render_template("product.html",params = params)

@app.route("/about")
def about():
    return render_template("about.html",params=params)
app.run(debug = True)