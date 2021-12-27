-- Die Kunden, die Artikel gekauft haben, deren Artikeltypen auch von einem Schweizer Lieferanten verfugbar sind. (Die Lösung hat 1286 Zeilen)
-- bietet an!!!!


-- -- Die Kunden, die Artikel gekauft haben,
-- SELECT COUNT(DISTINCT kauft.kid) FROM kauft 
-- -- deren Artikeltypen in der Liste zu finden ist mit...
-- INNER JOIN artikel ON artikel.aid = kauft.aid 
-- WHERE artikel.typid IN (
--     -- ...Artikel, die von Schweizer Lieferanten sind (gibt aber alle Artikel zurück --> stimmt das so?)
--     SELECT artikel.typid FROM artikel 
--     INNER JOIN lieferant on artikel.lid = lieferant.lid 
--     WHERE lieferant.land = 'Schweiz'
-- );


-- Die Kunden, die Artikel gekauft haben,
SELECT COUNT(DISTINCT kauft.kid) FROM kauft 
-- deren Artikeltypen in der Liste zu finden ist mit...
INNER JOIN artikel ON artikel.aid = kauft.aid 
WHERE artikel.typid IN (
    SELECT DISTINCT artikel.typid from artikel 
    NATURAL JOIN bietetan 
    NATURAL JOIN lieferant 
    WHERE lieferant.land = 'Schweiz'
);