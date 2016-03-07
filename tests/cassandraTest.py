from cassandra.cluster import Cluster
cluster = Cluster()
#the keyspace name is list
session = cluster.connect('list')

'''
CREATE TABLE list.tasks (
    id int PRIMARY KEY,
    creationtime text,
    endtime int,
    name text,
    postponecount int,
    priority int,
    status text,
    title text)

INSERT INTO tasks JSON '     {  
          "name":"basheer",
          "id": 3,
          "title": "go shopping",
          "priority":3,
          "creationTime": "10",
          "endTime": 24,
          "status":"incomplete",
          "postponeCount":1
        }';
'''
result=session.execute("""select * from tasks""")
for r in result:
	print r