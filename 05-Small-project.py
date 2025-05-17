from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/successif<int:score>")
def successif(score):
    res =""
    if score >=50:
        res = 'PASS'
    else:
        res = 'FAIL'

    final_res = {"Score ": score, "result":res }

    return render_template('results.html' ,results = final_res)


@app.route('/submit' ,methods = ['GET','POST'])
def submit():
    total_score=0
    if request.method == 'POST':
        Science = float(request.form['science'])
        maths = float(request.form['maths'])
        physics = float(request.form['physics'])
        
        total_score = float(Science+maths+physics)/3
    else:
        return render_template('get_marks.html')

    return redirect(url_for('successif',score = total_score))


if __name__ == "__main__":
    app.run()