## Name
# twc3_monitor

## Description
liest json von der Tesla Wallbox Version 3 iterativ ein, 

## Visuals
Dashboard Beispiele

![Dashboard](/media/Auswahl_20240507_003.png "ein aktiver Ladevorgang")

mobiles Dashboard

![mobile](/media/twc3_mobile_Ladestatus.jpg "was wurde schon geladen")

![mobile](/media/twc3_mobile_Ladeleistung.jpg "Ladeleistung")

![mobile](/media/twc3_mobile_Lademenge-Verbindung.jpg "Lademenge")

![mobile](/media/twc3_mobile_Temperaturen.jpg "Lademenge")


## Installation
Das Python-Skript auf einen Mini-Rechner, NAS oder Raspberry kopieren.

In der InfluxDB die Datenbank mit User und Passwort, wie in der ersten Zeilen des Python-Codes angegeben, anlegen.
In Grafana eine Datenquelle InfluxDB-twc3 anlegen und das Dashboard als .json einlesen.

## Usage
das Python-Skript in der /etc/crontab alle 1 oder 2 Minuten aufrufen.

`*/2 *  * * *  zotac   /usr/bin/python3 /home/zotac/pythonscripte/twc3.py`
## Support
pf@nc-x.com

## Contributing
open to contributions 

## License
MIT

## Project status
abgeschlossen, macht was es soll. Möglicherweise noch ein paar Anpassungen am Dashboard in Grafana.
