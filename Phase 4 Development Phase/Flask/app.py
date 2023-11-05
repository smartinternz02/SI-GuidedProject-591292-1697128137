from flask import Flask, request, render_template
import numpy as np
import pickle as pkl

model = pkl.load(open("/Phase 4 Development Phase/Training/model.pkl", 'rb'))

app = Flask(__name__)


@app.route("/")
def about():
    return render_template("home.html")


@app.route("/home")
def about1():
    return render_template("home.html")


@app.route("/predict")
def home1():
    return render_template("predict.html")


# def predict():
#     x = [[x for x in request.form.values()]]
#     print(x)
#
#     x = np.array(x)
#     print(x.shape)
#     print(x)
#
#     pred = model.predict(x)
#     print(pred[0])
#
#     return render_template("submit.html", prediction_text=str(pred))

@app.route('/predict', methods=['POST'])
def predict():

    # Get user input from the form
    feature1 = float(request.form['step'])
    feature2 = float(request.form['type'])
    feature3 = float(request.form['amount'])
    feature4 = float(request.form['oldbalanceOrg'])
    feature5 = float(request.form['newbalanceOrg'])
    feature6 = float(request.form['oldbalanceDest'])
    feature7 = float(request.form['newbalanceDest'])

    # Make a prediction using the loaded model
    prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])

    return f'The given payment : {prediction[0]}'


if __name__ == "__main__":
    app.run(debug=True)
