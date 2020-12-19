import json
import requests
from os import getcwd

from configparser import ConfigParser


def test_service(host, port, route, data):
    url = "http://{0}:{1}/{2}".format(host, port, route)
    response = requests.post(url=url, json=data)
    status = "200 OK" if response.status_code == 200 else str(response.status_code) + " ERROR"
    return "Response ({0}): {1}".format(status, response.text)


if __name__ == '__main__':
    config = ConfigParser()
    config.read('configs/app.ini')
    host, port = config['WEB']['host'], config['WEB']['port']

    current_dir = getcwd()
    data_path = 'tests/data/' + 'test_sents.json'
    with open(file=data_path) as fp:
        texts = json.load(fp)

    for s in texts:
        print('Attempting request /tokenize with data ["{0}"]'.format(s))
        result = test_service(host, port, '/tokenize', [s])
        print(result)

    print('Attempting request /tokenize with all data')
    result = test_service(host, port, '/tokenize', texts)
    print(result)