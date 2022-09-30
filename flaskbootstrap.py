from flask import *

#Create an instance (app)
app=Flask("__name__")

#Flask BootStrap
@app.route("/bootstrapexample")
def sample():
    return render_template('bootstraphome.html')

#main method
if __name__=="__main__":
    app.run()
