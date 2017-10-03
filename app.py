#Kelly Wang
#SoftDev1 pd7
#HW06: Echo Echo Echo . .
#2017-10-02

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    print "-----------------------APP "
    print app
    print "-----------------------REQUEST"
    print request
    print "-----------------------HEADERS "
    print request.headers
    print "-----------------------METHOD "
    print request.method
    print "-----------------------ARGS "
    print request.args
    print "-----------------------FORM "
    print request.form
    print "____________________DONE_____________________"
    return render_template('form.html')

@app.route("/hello")
def notCool():
    return render_template('coolForm.html',name=request.args["youName"] )

if __name__ == "__main__":
    app.debug = True
    app.run()
