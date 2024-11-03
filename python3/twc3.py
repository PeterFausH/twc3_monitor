# Liest die API von Tesla Wall connnector 3 ein.
# Iteriert durch (fast) alle JSON Datensätze
# Aufruf: python3 twc3.py
# pf@nc-x.com, Peter Fürle, Schwarzwald
# V1.0 vom 05.05.2024
import sys
import requests
import json
from influxdb import InfluxDBClient
# Configure InfluxDB connection variables
host = "127.0.0.1" 
port = 8086
user = "tessica"
password = "elon"
dbname = "twc3"
# Influx Datenbank verbinden
influx_client = InfluxDBClient(host, port, user, password, dbname)

# Jeder Bereich bekommt sein eigenes measurement (vitals, lifetime, wifi)
## [{'measurement': 'vitals',       'fields': {'revision': 0}}]
def eintragen(measurement,bez,wert):
    data=[{"measurement": measurement,"fields": {bez : wert}}]
    #print(data)
    if bez == "current_alerts" or bez == "evse_not_ready_reasons":
        print(measurement, bez,"ignored")
    else:
        influx_client.write_points(data, time_precision='m')
    return

# prüfen ob Wert numerisch sein könnte, sonst String
def num(s):
    try:
        return float(s)
    except ValueError:
        return s

# json aufdröseln und zum Eintragen in die Datenbank weitergeben.
def iter_dict(data, endpoint):
    for key, value in data.items():
        eintragen(str(endpoint),str(key),value)

#Api vom Wallconnector abrufen
def hole(endpoint):
  r = requests.get("http://192.168.20.133/api/1/"+endpoint)
  parsed_json = json.loads(r.text)
  iter_dict(parsed_json,endpoint)

# MAIN #
# Bereiche zum parsen übergeben (vitals, lifetime, wifi_status, version)
hole("lifetime")
hole("wifi_status")
hole("version")
hole("vitals")
