<h2>Marine-animals-vizualization</h2>
<h4><i>This is a project in which we scrapped marine animals data from a website and then vizualized using neo4j database and created relationships to understand it better.</i></h4>

<h3> Neo4J commands to manipulate data and create relationships</h3>
<h3>Remove Duplicated</h3>
<p> MATCH (n:feed_habits) WITH n.Feeding_Habits AS habit, collect(n) AS DUPLICATES
    WHERE size(duplicates) >  1 FOREACH (n in tail(duplicates) | DELETE n)
</p>

<h3> Connect all the marine animals using "habitat" ecosystem edge.</h3>
<p> MATCH (n:Marine),(m:Marine)
    WHERE NOT m=n and n.Habitat=m.Habitat CREATE (m)-[r:neighbor]->(n) RETURN r
</p>

<h3> Connect all marine animals to feeding habits with an edge.</h3>
<p> MATCH (m:Marine),(f:feed_habits)
    WHERE m.feed_habits=f.feed_habits CREATE (m)-[r:Identical_Feeding_Habits_]->(f) RETURN r
</p>

<h3>Show the animals which are endangered </h3>
<p> There are 2 commands that does this thing. <br>
    1. 
    MATCH (n)
    WHERE n.ConservationStatus contains 'Endangered' RETURN n
    <br>
    2.
    MATCH (m:Marine),(n:feed_habits) WHERE m.ConservationStatus contains 'Endangered'  and m.Feeding_Habits = n.Feeding_Habits RETURN m,n
</p>
