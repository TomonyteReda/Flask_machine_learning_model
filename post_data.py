import requests
from argparse import ArgumentParser


def get_argument():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('-l', type=str)
    args = argument_parser.parse_args()
    l = args.l
    measures = [float(item) for item in l.split(',')]
    print(measures)
    return measures


def create_dictionary():
    measure_names = ['s_length', 's_width', 'p_length', 'p_width']
    measures = get_argument()
    payload = dict(zip(measure_names, measures))
    return payload


def post_data_request():
    payload = create_dictionary()
    r = requests.post("http://172.20.34.206:8080/iris", json=payload)
    # print(f"Status Code: {r.status_code}, Response: {r.json()}")


post_data_request()
