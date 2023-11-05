from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle as pkl

model = pkl.load(open("Phase 4 Development Phase/Training", 'rb'))

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("Phase 4 Development Phase/Flask/templates/home.html")

@app.route("/home")
def about1():
    return render_template("Phase 4 Development Phase/Flask/templates/home.html")
