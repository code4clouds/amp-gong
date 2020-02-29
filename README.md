# amp-gong
Azure Marketplace Automated Achievement Gong

## Installation

``` bash
apt-get install -y python3 python3-pip azure-servicebus
pip3 install -r requirements.txt
chmod +x start.sh
chmod +x cron.sh
```

## Execution

``` bash
./start.sh
```

## Upgrades

```
sh ./upgrade.sh
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
