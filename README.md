# amp-gong
Azure Marketplace Automated Achievement Gong

## Installation

``` bash
chmod +x setup.sh
sudo ./setup.sh
```

## Execution

``` bash
chmod +x start.sh
./start.sh
```

## Upgrades

```
chmod +x ./upgrade.sh
./upgrade.sh
```

## Onboot

```
chmod +x cron.sh
crontab -e
```

Then add the following line
```
@reboot sleep 60 && /home/pi/amp-gong/cron.sh
```

## Development
