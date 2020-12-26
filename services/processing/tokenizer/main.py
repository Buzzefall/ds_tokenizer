import logging
import time

from redis.client import Redis

from nlp.tokenize import Tokenizer


def get_data(client: Redis):
    text_keys = client.hkeys('texts_to_tokenize')
    texts = client.hmget('texts_to_tokenize', text_keys)
    logging.info("Got {0} keys from Redis".format(len(text_keys)))

    return text_keys, texts


if __name__ == '__main__':
    logging.basicConfig(filename='/data/logs/service-tokenizer.log', level=logging.INFO, filemode='r+')

    print("Starting Tokenizer service...")
    logging.info("Starting Tokenizer service...")
    time.sleep(3)

    redis = Redis(host='redis', port=6379)
    keys, sents = get_data(redis)

    print(str(keys), str(sents))

    tzr = Tokenizer()
    for key, sent in zip(keys, sents):
        msg = "Tokenizing input: {0}".format(sent)
        print(msg)
        logging.info(msg)

        result = tzr.process(sent)

        msg = "Output: {0}\n".format(result)
        print(msg)
        logging.info(msg)

    for key in keys:
        redis.hdel('texts_to_tokenize', key)

    keys = redis.hgetall('texts_to_tokenize')
    logging.info("Redis contains {0} keys now".format(len(keys)))

    print("Shutting down Tokenizer service...")
    logging.info("Shutting down Tokenizer service...")

    redis.close()
