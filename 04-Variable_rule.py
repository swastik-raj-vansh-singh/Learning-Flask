# from flask import Flask 

# app = Flask(__name__)

# @app.route('/submit/<int:score>')
# def submit(score):
#     return ("the marks is " + str(score))

# if __name__ == "__main__":
#     app.run(debug = True)

# the above code will give if i give /submit/55 -- the marks is 55



##leaning the jinga template
# from flask import Flask ,render_template
# app = Flask(__name__)

# # @app.route('/submit/<int:marks>')
# # def submit(marks):
# #     return ("the marks is " + str(marks))

# @app.route('/success/<int:score>')
# def submit(score):
#     res = ""
#     if score > 50:
#         res = "pass"
#     else:
#         res = "Fail"
#     return render_template('result.html',results = res)


# if __name__ == "__main__":
#     app.run(debug = True)




from flask import Flask ,render_template
app = Flask(__name__)

# @app.route('/submit/<int:marks>')
# def submit(marks):
#     return ("the marks is " + str(marks))

@app.route('/success1/<int:score>')
def submit(score):
    res = ""
    if score > 50:
        res = "pass"
    else:
        res = "Fail"
    exp = {"score" :score,"res":res}
    
    return render_template('results.html',results = exp)


if __name__ == "__main__":
    app.run(debug = True)