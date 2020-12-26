import logging
from redis.client import Redis

from nlp.tokenize import Tokenizer


def get_data(client: Redis):
    text_keys = client.hkeys('texts_to_tokenize')
    logging.debug("Got {0} keys from Redis".format(len(text_keys)))

    texts = client.mget(text_keys)

    return text_keys, texts


if __name__ == '__main__':
    logging.basicConfig(filename='/data/logs/service-tokenizer.log')

    print("Starting Tokenizer service...")
    logging.info("Starting Tokenizer service...")

    redis = Redis(host='redis', port=6379)
    keys, sents = get_data(redis)

    with Tokenizer() as tzr:
        for key, sent in zip(keys, sents):
            msg = "Tokenizing input: {0}".format(sent)
            print(msg)
            logging.debug(msg)

            result = tzr.process(sent)

            msg = "Output: {0}\n".format(result)
            print(msg)
            logging.debug(msg)

    redis.hdel('texts_to_tokenize', keys)

    keys = redis.hgetall('texts_to_tokenize')
    logging.debug("Redis contains {0} keys now".format(len(keys)))

    print("Shutting down Tokenizer service...")
    logging.info("Shutting down Tokenizer service...")

    redis.close()
