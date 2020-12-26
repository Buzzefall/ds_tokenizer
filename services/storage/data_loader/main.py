import json
import logging

from redis.client import Redis


if __name__ == '__main__':
    logging.basicConfig(filename='/data/logs/service-data_loader.log')

    print("Starting Loader service...")
    logging.info("Starting Loader service...")

    redis = Redis(host='redis', port=6379)

    with open(file='/data/test_sents.json') as fp:
        texts = json.load(fp)

    msg = "Uploading data for processing: {0}".format(str(texts))
    print(msg)
    logging.debug(msg)

    redis.hset(name='texts_to_tokenize', mapping=texts)

    print("Shutting down Tokenizer service...")
    logging.info("Shutting down Tokenizer service...")

    redis.close()
