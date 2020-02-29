#!/bin/bash
source .env
export QUEUE_NAME=$QUEUE_NAME
export QUEUE_CONNECTION_STRING=$QUEUE_CONNECTION_STRING
python3 gong.py
