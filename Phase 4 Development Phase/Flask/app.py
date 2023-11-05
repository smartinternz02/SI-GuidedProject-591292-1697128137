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


def predict():
    x = [[x for x in request.form.values()]]
    print(x)

    x = np.array(x)
    print(x.shape)
    print(x)

    pred = model.predict(x)
    print(pred[0])

    return render_template("submit.html", prediction_text=str(pred))


if __name__ == "__main__":
    app.run(debug=True)
