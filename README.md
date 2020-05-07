# Marine-animals-vizualization
This repoThis is a project in which we scrapped marine animals data from a website and then vizualized using neo4j database and created relationships to understand it better.


duplicates remove :
    MATCH (n:feed_habits) WITH n.Feeding_Habits as habit, collect(n) AS duplicates
    WHERE size(duplicates) >  1 FOREACH (n in tail(duplicates) | DELETE n)

4.match (n:Marine),(m:Marine)
    where not m=n and n.Habitat=m.Habitat create (m)-[r:neighbor]->(n) return r

5.match (m:Marine),(f:feed_habits)
    where m.feed_habits=f.feed_habits create (m)-[r:Identical_Feeding_Habits_]->(f) return r

6(a)
    match (n)
    where n.ConservationStatus contains 'Endangered' return n

6(b)
    match (m:Marine),(n:feed_habits) where m.ConservationStatus contains 'Endangered'  and m.Feeding_Habits = n.Feeding_Habits return m,n