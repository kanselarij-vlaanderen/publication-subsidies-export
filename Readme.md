# Subsidiedossiers export


De dossiers met nummer “0-subsidie” moeten niet omgezet worden naar Kaleidos en de publicatie-module. 

We schrijven ze weg in een CSV-bestand met volgende velden:
  - titel (Opschrift)
  - Trefwoord
  - Opdrachtgever
  - Datum beslissing
  - Datum ontvangst
  - Aantal bladzijden
  - Beleidsdomein
  - Minister
  - Opmerkingen
  - Document naam
  - Datum Vloeiboek ontvangen
  - Datum Vloeiboek naar m-p
  - Datum Vloeiboek terug van m-p
  - Datum Verspreiding


```sh
docker build -t "ovrb-subsidie-export" .
docker run -v "/path/to/access/export/folder:/data" ovrb-subsidie-export
```

output will appear aside the xml input file.
