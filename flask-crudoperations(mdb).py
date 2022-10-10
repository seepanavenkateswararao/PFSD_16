from flask import *

from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017")

db=client['STUDENT']
studentdetails=db.details

app=Flask("__name__")

@app.route("/crudexample")
def sample():
    return render_template('form.html')

@app.route("/successfull",methods=('GET','POST'))
def sample1():
    fn=request.form.get('fn')
    ln=request.form.get('ln')
    rno=request.form.get('rno')
    mb=request.form.get('mb')
    a={"first name":fn,"last name":ln,"reg no":rno,"mobile no":mb}
    studentdetails.insert_one(a)

    return "Successfully Inserted"

#main method
if __name__=="__main__":
    app.run()


# 8500103040-->sir numbers
# 8500105060