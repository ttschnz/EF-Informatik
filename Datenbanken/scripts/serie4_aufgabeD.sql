-- Alle Bezeichnungen von nicht mehr in Filialen lagernden Artikeltypen und deren Anzahl. (Die Lösung hat 19 Zeilen)
SELECT COUNT(artikel.typid), artikeltyp.bezeichnung 
FROM artikel 
NATURAL JOIN artikeltyp 
WHERE artikel.fid IS NULL 
GROUP BY artikeltyp.bezeichnung; 