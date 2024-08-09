MATCH (i:Item)-[r:HAS_CONTRIBUTOR]-(c:Contributor)
WHERE c.contributor <> "supreme court of the united states"
OPTIONAL MATCH (i)-[s:HAS_SUBJECT]->(sub:Subject)
WITH c, sub, COUNT(i) AS item_count, COLLECT(sub) AS subjects
WHERE sub IS NOT NULL
MERGE (c)-[:WROTE_ABOUT]->(sub)
RETURN c, item_count, subjects;
