#!/usr/python3

import time, sys, os
from azure.servicebus import QueueClient, Message

# Create the QueueClient
if('QUEUE_CONNECTION_STRING' in os.environ and 'QUEUE_NAME' in os.environ):
    queue_client = QueueClient.from_connection_string(os.environ.get("QUEUE_CONNECTION_STRING"), os.environ.get("QUEUE_NAME"))

    # Receive the message from the queue
    while(True):
        with queue_client.get_receiver() as queue_receiver:
            messages = queue_receiver.fetch_next(timeout=3)
            for message in messages:
                print("turn on relay")
                message.complete()
        time.sleep(30)

else:
    print('Please add the QUEUE_CONNECTION_STRING and QUEUE_NAME to the environment')