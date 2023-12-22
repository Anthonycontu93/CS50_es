SELECT m.title
FROM movies m
INNER JOIN stars s1   ON m.id = s1.movie_id
INNER JOIN people p1  ON s1.person_id = p1.id AND p1."name" = 'Johnny Depp'
INNER JOIN stars s2   ON m.id = s2.movie_id
INNER JOIN people p2  ON s2.person_id = p2.id AND p2."name" = 'Helena Bonham Carter';