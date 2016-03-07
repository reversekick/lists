#!/usr/bin/env python
import web
import json
from cassandra.cluster import Cluster


cluster=Cluster()
session = cluster.connect('list')

urls = (
    '/all','get_all_user',
    '/task/(.*)','get_task'
)

app = web.application(urls, globals())

class get_all_user:
    def GET(self):
     query="select * from tasks"   
     queryResult=session.execute(query) 
     result="id name tittle priority creationTime endTime status postponeCount\n"
     for r in queryResult:
        result+=str(r.id)+" "+str(r.name)+" "+str(r.title)+" "+str(r.creationtime)+" "+str(r.endtime)+" "+str(r.status)+" "+str(r.postponecount)+"\n"
     print result
     return result


class get_task:
    def GET(self,user):
        if len(user)==0:
            return "Usage:http://localhost:8080/task/arg1:name of user"
       
        print "Username:",user
        query="""select * from tasks where name='"""+user+"""'"""   
        queryResult=session.execute(query)
        result="id name tittle priority creationTime endTime status postponeCount\n"
        for r in queryResult:
            result+=str(r.id)+" "+str(r.name)+" "+str(r.title)+" "+str(r.creationtime)+" "+str(r.endtime)+" "+str(r.status)+" "+str(r.postponecount)+"\n"
        print result
        return result
       
    def POST(self):
        data = web.data()
        print "New POST:",data
        session.execute("""insert into tasks JSON '"""+str(data)+"""'""")
if __name__ == "__main__":
    app.run()