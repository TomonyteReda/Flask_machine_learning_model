from flask import Flask, request, send_file, redirect
import pickle
import pandas as pd
from random_forest_classifier import get_prediction

app = Flask(__name__)


def load_measures_from_file():
    with open("measures.pickle", "rb") as f:
        d = pickle.load(f)
    list_of_values = [d[key] for key in d if type(d[key]) == float]
    return list_of_values


def show_iris_image(prediction):
    return send_file(f"{prediction}.jpg", mimetype='image/jpeg')


@app.route("/setosa")
def setosa():
    return send_file("setosa.jpg", mimetype='image/jpeg')


@app.route("/versicolor")
def versicolor():
    return send_file("versicolor.jpg", mimetype='image/jpeg')


@app.route("/virginica")
def virginica():
    return send_file("virginica.jpg", mimetype='image/jpeg')


@app.route('/iris', methods=['GET', 'POST'])
def process_json():
    d = {}
    content = request.json
    d['s_length'] = content['s_length']
    d['s_width'] = content['s_width']
    d['p_length'] = content['p_length']
    d['p_width'] = content['p_width']
    with open("measures.pickle", "wb") as f:
        pickle.dump(d, f)
    return "Success"


@app.route('/predict')
def predict():
    list_of_values = load_measures_from_file()
    print(list_of_values)
    if len(list_of_values) < 4:
        return "Please enter float type measures"
    else:
        prediction = get_prediction(list_of_values)
        prediction = str(prediction[0])
        show_iris_image(prediction)
        return redirect(f'/{prediction}')


if __name__ == "__main__":
    app.run(host="172.20.34.206", port=8080, debug=True)

