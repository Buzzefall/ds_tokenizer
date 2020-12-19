from flask import Flask, request, jsonify
from configparser import ConfigParser

from src.tokenize import Tokenizer

tokenizer = Tokenizer()
app = Flask(__name__)


@app.route('/tokenize', methods=['POST'])
def tokenize():
    sents = request.json
    sents_tokenized = []
    for s in sents:
        s_tokenized = tokenizer.process(s)
        sents_tokenized.append(s_tokenized)

    return jsonify(sents_tokenized)


if __name__ == '__main__':
    config = ConfigParser()
    config.read('configs/app.ini')

    app.run(host=config['WEB']['host'], port=config['WEB']['port'])
