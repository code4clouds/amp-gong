#!/bin/bash
apt-get install -y python3 python3-pip azure-servicebus
pip3 install -r requirements.txt
chmod +x start.sh
chmod +x setup.sh
chmod +x cron.sh