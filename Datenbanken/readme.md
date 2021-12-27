# postgreSQL
## Installation
1. [install docker](https://docs.docker.com/engine/install/)
2. clone this repo: `git clone https://github.com/ttschnz/EF-Informatik`
3. cd to this folder: `cd EF-Informatik/Datenbanken`
4. follow instructions on usage

## Usage
start server:
```
docker compose up
```
enter terminal:
```
docker exec -it db "/bin/sh"
su - postgres
cd /scripts
psql
```
___
## Commands
|command|description|
|--|--|
| `\! cls` or `\! clear` | clear screen| 
| `\l` | list dbs | 
|`\c [name]` | change db|
| `\d [name]` | show relations|
| `\i [path]` | execute file | 
___
## Aufgaben Serie 4
1. Erstellen Sie mit PostgreSQL eine Datenbank Konzern mit den folgenden sieben relationalen Datenbankschemata
``` sql
Artikel(
    AId : INTEGER,
    FIdo: INTEGER −→ Filiale,
    TypId : INTEGER −→ Artikeltyp,
    LId : INTEGER −→ Lieferant 
)

Artikeltyp(
    TypId : INTEGER,
    Bezeichnung : VARCHAR(100),
    Preis : NUMERIC(10,2)
)

Lieferant(
    LId : INTEGER,
    Name : VARCHAR(50),
    Land : VARCHAR(50) 
)

Filiale(
    FId : INTEGER,
    Filialleiter : VARCHAR(50),
    Adresse : VARCHAR(100)
)

Kunde(
    KId : INTEGER,
    Steuerreferenz : VARCHAR(50)
)

bietetan(
    TypId : INTEGER −→ Artikeltyp,
    LId : INTEGER −→ Lieferant,
    Angebotspreis : NUMERIC(10,2) 
)

kauft(
    AId : INTEGER −→ Artikel,
    KId : INTEGER −→ Kunde,
    Datum : TIMESTAMP 
)
```
Lösung:
[sqlfile](scripts/serie4_setup.sql)
___
### Fügen Sie die Tupel der Datei Testdaten.sql in die Datenbank ein

[sqlfile](scripts/serie4_data.sql)
___
### Finden Sie SQL-Abfragen, die die folgenden Informationen abfragen:
**a) Alle Filialleiter, welche Artikel vom Lieferanten "Druckwerk Trallala" beziehen (Die richtige Lösung liefert 4 Zeilen)**
___
```sql
SELECT DISTINCT filialleiter FROM lieferant INNER JOIN  artikel ON artikel.lid = lieferant.lid INNER JOIN filiale ON filiale.fid = artikel.fid WHERE lieferant.name = 'Druckwerk Trallala';
SELECT DISTINCT filialleiter FROM lieferant 
INNER JOIN  artikel ON artikel.lid = lieferant.lid 
INNER JOIN filiale ON filiale.fid = artikel.fid 
WHERE lieferant.name = 'Druckwerk Trallala';

-- =>
-- filialleiter  
-- ----------------
-- Arnold Fischer
-- Bernd Leitner
-- Karl Seeberg
-- Paul Kreuter
-- (4 rows)
```
___

**b) Alle Kunden, die einen Artikel gekauft haben, der nicht von einer
Schweizer Firma produziert wird (Die richtige Lösung liefert 992
Zeilen)**

```sql
SELECT COUNT(DISTINCT kauft.kid) FROM kauft 
INNER JOIN artikel on artikel.aid = kauft.aid 
WHERE artikel.lid IN (
    SELECT lieferant.lid FROM lieferant WHERE lieferant.land != 'Schweiz'
);
-- => 992
```
___

**c) Die Kunden, die Artikel gekauft haben, deren Artikeltypen auch
von einem Schweizer Lieferanten verfugbar sind. (Die Lösung hat
1286 Zeilen)**
```sql
SELECT COUNT(DISTINCT kauft.kid) FROM kauft 
INNER JOIN artikel ON artikel.aid = kauft.aid 
WHERE artikel.typid IN (
    SELECT DISTINCT artikel.typid from artikel 
    NATURAL JOIN bietetan 
    NATURAL JOIN lieferant 
    WHERE lieferant.land = 'Schweiz'
);
-- => 1286
```
___
**d) Alle Bezeichnungen von nicht mehr in Filialen lagernden Artikeltypen und deren Anzahl. (Die Lösung hat 19 Zeilen)**
```sql
SELECT COUNT(artikel.typid), artikeltyp.bezeichnung 
FROM artikel 
NATURAL JOIN artikeltyp 
WHERE artikel.fid IS NULL 
GROUP BY artikeltyp.bezeichnung; 

-- => 
-- count |                           bezeichnung
-- -------+------------------------------------------------------------------
--     74 | Siebdruck Unter den Talaren""
--     95 | Plakat: Bessere Hochschulmensen (vegane Fassung)
--     99 | Jagdtrophaeen Durchgefallene Studenten""
--    108 | Tierknochen (nicht Pferd!!)
--     85 | Datenbank Erfundenes, das vorgibt Kunst zu sein!""
--     89 | Jagdtrophaeen Erwischte Plagiatoren""
--     88 | Utopie vorbereiteter Student""
--     94 | Das liest sowieso niemand
--     77 | Unsinn in einer Datenbank
--     82 | Siebdruck Moderner Student""
--    102 | Plastikserie Bruellende Schreie""
--  ...
-- 
-- (19 rows)
``` 
___

**e) Zu jedem Kunden das Total (die Summe der Preise) bereits gekaufter Artikel, wenn er sie zu aktuellen Preisen kaufen würde.
(Der Kunde mit der Kundennummer 8 hat für 20111.25 Franken eingekauft und es hat insgesamt 1414 Kunden)**
```sql
SELECT SUM(preis), kid FROM kauft 
NATURAL JOIN kunde
NATURAL JOIN artikel
NATURAL JOIN artikeltyp
GROUP BY kid
-- ORDER BY kid => für Kontrolle bei Kunde 8
;
```
