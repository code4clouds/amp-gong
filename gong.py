#!/usr/python3

import time, sys, os
from azure.servicebus import QueueClient, Message
import RPi.GPIO as GPIO


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

# Setup GPIO Channels
Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)

# Create teh service bus connection
queue_client = QueueClient.from_connection_string(QUEUE_CONNECTION_STRING, QUEUE_NAME)

# Receive the message from the queue
while(True):
    with queue_client.get_receiver() as messages:
        for message in messages:
            print(message)
            try:
                #Control the Channel 1
                GPIO.output(Relay_Ch1,GPIO.LOW)
                print("Channel 1:The Common Contact is access to the Normal Open Contact!")
                time.sleep(0.5)

                GPIO.output(Relay_Ch1,GPIO.HIGH)
                print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
                time.sleep(0.5)
                # Remove message from queue
                message.complete()  
            except:
                print("except")
                GPIO.cleanup()
