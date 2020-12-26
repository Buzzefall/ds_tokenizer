#!/bin/bash

# Run docker container
echo "Running ds_tokenizer in detached mode..."
docker run -d -p 7620:7620 ds_tokenizer