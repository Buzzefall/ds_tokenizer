from flask import Flask, request, jsonify

from helpers.fs_utils import get_app_config
from nlp.tokenize import Tokenizer

tokenizer = Tokenizer()
app = Flask("DS Tokenizer")


@app.route('/tokenize', methods=['POST'])
def tokenize():
    sents = request.json
    sents_tokenized = []
    for s in sents:
        s_tokenized = tokenizer.process(s)
        sents_tokenized.append(s_tokenized)

    return jsonify(sents_tokenized)


if __name__ == '__main__':
    config = get_app_config()
    app.run(host=config['WEB']['host'], port=config['WEB']['port'])
