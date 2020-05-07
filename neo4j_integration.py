__author__ = 'Harsh'
import pickle
from neo4j import GraphDatabase

def run():
    db = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    f=open("scraped_data.json","rb")
    list=pickle.load(f)
    count=0
    for i in list:
        try:
            db.session().run("Create ( ma:Marine {  Name: '%s' ,Bio_Name: '%s', Habitat: '%s',ConservationStatus:'%s',Feeding_Habits: '%s',type:'ma' })" % (i['Name'],i['Bio-name'],i['Ecosystem/Habitat'],i['Conservation Status'],i['Feeding Habits']))
            db.session().run("Create ( fh:feed_habits { Feeding_Habits: '%s'})" % i['Feeding Habits'])
        except:
            db.session().run("Create ( ma:Marine {  Name: '%s' ,Bio_Name: '%s', Habitat: '%s',Feeding_Habits: '%s',type:'ma' })" % (i['Name'],i['Bio-name'],i['Ecosystem/Habitat'],i['Feeding Habits']))
            db.session().run("Create ( fh:feed_habits { Feeding_Habits: '%s'})" % i['Feeding Habits'])

        print(count)
        count+=1
run()

"""
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
"""