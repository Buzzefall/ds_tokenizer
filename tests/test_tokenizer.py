from src.tokenize import Tokenizer
import json


def test_tokenizer(sentence: str):
    result = tokenizer.process(sentence)
    print(result)


if __name__ == '__main__':
    with open(file='data/test_sents.json') as fp:
        texts = json.load(fp)

    tokenizer = Tokenizer()

    for s in texts:
        test_tokenizer(s)
