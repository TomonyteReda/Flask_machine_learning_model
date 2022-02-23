import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


def save_random_forest_model():
    iris = sns.load_dataset('iris')
    cols = iris.columns.tolist()
    X = iris[cols[:-1]]
    y = iris['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    model = RandomForestClassifier().fit(X_train, y_train)
    with open("iris_predictor.pickle", "wb") as f:
        pickle.dump(model, f)


def get_prediction(list_of_values):
    with open("iris_predictor.pickle", "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([list_of_values])
    return prediction


save_random_forest_model()





