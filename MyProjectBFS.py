from flask import *
#Create an instance (app)
app=Flask("__name__")
#Flask BootStrap
@app.route("/")
def sample():
    return render_template('MyProjectHome.html')
@app.route("/signup")
def sample2():
    return render_template('MyProjectSignup.html')
@app.route("/login")
def sample3():
    return render_template('MyProjectLogin.html')

#main method
if __name__=="__main__":
    app.run()
