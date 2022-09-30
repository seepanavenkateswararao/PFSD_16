#import flask
from flask import Flask,render_template,url_for,redirect

#Create an instance (app)
app=Flask(__name__)

#Route (End Point)
@app.route('/')

#method defining
def sample():
    return "<h1>This is my First Preactice Website </h1> " \
           "<button>sample1</button>"


#dynamic Routing
@app.route("/<name>")

def sample1(name):
    return f'Hello {name}'

#flask tamplet rendering
@app.route("/templates")

def sample2():
    return render_template('sample.html')

#flask context passing to tamplets
@app.route("/template1/<name>")
def sample3(name):
    return render_template('index2.html',name=name)

#flask Redirect
@app.route("/route/template2/<role>")
def sample4(role):
    if role=="guest":
        return redirect(url_for('sample2'))
    else:
        return redirect(url_for('sample3',name=role))

#List Rendering with for tag
@app.route("/list/rendering")
def sample5():
    lst=['abc','def','ghi']
    return render_template('index3.html',name=lst)


#main method
if __name__=="__main__":
    app.run()