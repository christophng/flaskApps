from flask import Flask, render_template, request
from wtforms import Form, IntegerField, FieldList, SubmitField

app = Flask(__name__)

# Main app
@app.route('/')
def index():
    return render_template('calculator.html')


@app.route('/result', methods = ['POST', 'GET'])
def result():

    gradeData = request.form.getlist("grade", type = int)
    weightData = request.form.getlist("weight", type = int)

    valueSum = 0
    weightSum = 0
    counter = 0

    while counter < len(gradeData):
        valueSum += (gradeData[counter]) * (weightData[counter])
        weightSum += (weightData[counter])
        counter += 1

    average = valueSum / weightSum

    return render_template("result.html", value = average)


if __name__ == '__main__':
    app.run(debug = True)
