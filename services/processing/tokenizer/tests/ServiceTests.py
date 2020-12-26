import json
import requests

from services.processing.tokenizer.helpers import get_app_config


class ServiceTest:
    @staticmethod
    def test_service(host, port, route, data):
        url = "http://{0}:{1}/{2}".format(host, port, route)
        response = requests.post(url=url, json=data)
        status = "200 OK" if response.status_code == 200 else str(response.status_code) + " ERROR"
        return "Response ({0}): {1}".format(status, response.text)

    @staticmethod
    def run():
        config = get_app_config()

        host, port = config['WEB']['host'], config['WEB']['port']

        data_path = 'tests/data/' + 'test_sents.json'
        with open(file=data_path) as fp:
            texts = json.load(fp)

        for s in texts:
            print('Attempting request /tokenize with data ["{0}"]'.format(s))
            result = ServiceTest.test_service(host, port, '/tokenize', [s])
            print(result)

        print('Attempting request /tokenize with all data')
        result = ServiceTest.test_service(host, port, '/tokenize', texts)
        print(result)
