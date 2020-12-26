from spacy.lang.en import English


class Tokenizer:
    def __init__(self):
        self.tokenizer = English()
        self.tokenizer.disable_pipes([pipe_name for pipe_name in self.tokenizer.pipe_names if pipe_name != 'tokenizer'])

        stop_words = set("!@#$%^&*()_+-=~`/\*'")
        for sw in stop_words:
            self.tokenizer.vocab[sw].is_stop = True

    def process(self, sentence):
        if type(sentence) == bytes:
            sentence = sentence.decode('utf-8')

        return ' '.join(token.text.lower() for token in self.tokenizer(sentence) if
                        not token.is_stop and not token.is_punct and not token.is_space and not token.is_digit)