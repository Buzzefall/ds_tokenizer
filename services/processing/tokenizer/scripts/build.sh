#!/bin/bash

echo "Building the ds_tokenizer docker image at $PWD"
docker build -t ds_tokenizer .
