# amp-gong
Azure Marketplace Automated Achievement Gong

## Hardware

- Raspberry 4
- Waveshare Raspberry Relay

## Azure Services

- Service Queue
- Logic Apps

## Installation

``` bash
apt-get update
apt-get install -y python3 python3-pip 
pip3 install azure-servicebus
pip3 install -r requirements.txt
chmod +x start.sh
chmod +x cron.sh
```

## Setup

```
cat >> .env
QUEUE_NAME=queue_name_here
QUEUE_CONNECTION_STRING=connection_string_here
EOF
```

## Execution

``` bash
./start.sh
```

## Upgrades

```
sh upgrade.sh
```

## Onboot

```
crontab -e
```

Then add the following line
```
@reboot sleep 60 && /home/pi/amp-gong/cron.sh
```

## Development
