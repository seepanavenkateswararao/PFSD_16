from flask import *
#Create an instance (app)
app=Flask("__name__")
#Flask BootStrap
@app.route("/")
def sample():
    return render_template('bootstraphome.html')
@app.route("/bootstraplogin")
def sample1():
    return render_template('bootstraplogin.html')
#main method
if __name__=="__main__":
    app.run()
