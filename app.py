### Create a simple flask application
from flask import Flask,render_template,request,redirect,url_for

### create the flask app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/success/<int:score>")
def success(score):
    return "<h1> the person is Pass and the score is " + str(score) + "</h1>"

@app.route("/fail/<int:score>")
def fail(score):
    return "<h1> the person has failed and the score is  " + str(score) + "</h1>"

@app.route("/calculate")
def calculate():
    return render_template('calculate.html')

@app.route("/cal", methods=['POST','GET'])
def cal():
    if request.method =='GET':
        return render_template('cal.html',results =0)
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        sum = (maths+science+history)/3
        result = ""
        if(sum>50):
            result = "success"
        else:
            result = "fail"

        #return redirect(url_for(result,score = sum))
        #return render_template('cal.html',results = sum)  #for same page
        return render_template('result.html',results = sum)  # another page



if __name__ == "__main__":
    app.run(debug=True)