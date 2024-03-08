#!/usr/bin/env python

import configparser
import json
import requests
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime, timezone

def loadConfigs():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def getNodeStats(config):
    url = "https://stats.allstarlink.org/api/stats/"+config['Node']['NodeNumber']
    response = json.loads(requests.get(url).text)
    return response

def main():
    config = loadConfigs()
    stats = getNodeStats(config)
    print(stats['stats']['data'])

    if config['influxdb']['UseSSL'] is True:
        influxProtocol="https://"
    else:
        influxProtocol="http://"
   
    client = influxdb_client.InfluxDBClient(url=influxProtocol+config['influxdb']['Host']+":"+config['influxdb']['Port'], token=config['influxdb']['Token'], org=config['influxdb']['Org'])
    query_api = client.query_api()
    write_api = client.write_api(write_options=SYNCHRONOUS)
    
    totalKeyUps = Point("totalKeyUps").tag("totalkeyups", stats['stats']['data']['totalkeyups']).field("totalKeyUps", int(stats['stats']['data']['totalkeyups'])).time(datetime.now(tz=timezone.utc), WritePrecision.MS)

    write_api.write(bucket=""+config['influxdb']['Bucket']+"", record=totalKeyUps)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt as e:
    print("\n\nExiting on user cancel.", file=sys.stderr)
    sys.exit(1)
