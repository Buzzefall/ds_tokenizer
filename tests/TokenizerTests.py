from nlp.tokenize import Tokenizer
import json


class TokenizerTest:

    @staticmethod
    def test_tokenizer(tokenizer, sentence: str):
        print("Tokenizing input: ", sentence)
        result = tokenizer.process(sentence)
        print("Output: ", result, '\n')

    @staticmethod
    def run():
        with open(file='tests/data/test_sents.json') as fp:
            texts = json.load(fp)

        tokenizer = Tokenizer()

        for s in texts:
            TokenizerTest.test_tokenizer(tokenizer, s)
