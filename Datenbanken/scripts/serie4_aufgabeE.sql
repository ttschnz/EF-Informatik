-- Zu jedem Kunden das Total (die Summe der Preise) bereits gekaufter Artikel, wenn er sie zu aktuellen Preisen kaufen würde.
-- (Der Kunde mit der Kundennummer 8 hat für 20111.25 Franken eingekauft und es hat insgesamt 1414 Kunden)

SELECT SUM(preis), kid FROM kauft 
NATURAL JOIN kunde
NATURAL JOIN artikel
NATURAL JOIN artikeltyp
GROUP BY kid
-- ORDER BY kid
;