SELECT COUNT(DISTINCT kauft.kid) FROM kauft 
INNER JOIN artikel on artikel.aid = kauft.aid 
WHERE artikel.lid IN (
    SELECT lieferant.lid FROM lieferant WHERE lieferant.land != 'Schweiz'
);