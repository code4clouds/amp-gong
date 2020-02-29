#!/usr/python3

import time, sys, os
from azure.servicebus import QueueClient, Message

# Create the QueueClient

# Get the Service Bus environmental variables
QUEUE_NAME = os.getenv("QUEUE_NAME", None)
QUEUE_CONNECTION_STRING = os.getenv("QUEUE_CONNECTION_STRING", None)

# Print a message to the user to let the know the environment is not ready
if QUEUE_NAME is None or QUEUE_CONNECTION_STRING is None:
    print('Please add the QUEUE_CONNECTION_STRING and QUEUE_NAME to the environment')
    exit(1)
else:
    # Pring the variables for debugging
    print('QUEUE_NAME:', QUEUE_NAME)
    print('QUEUE_CONNECTION_STRING:', QUEUE_CONNECTION_STRING)

    # Create teh service bus connection
    queue_client = QueueClient.from_connection_string(QUEUE_CONNECTION_STRING, QUEUE_NAME)

    # Receive the message from the queue
    while(True):
        with queue_client.get_receiver() as messages:
            for message in messages:
                print(message)
                message.complete()
