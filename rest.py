#!/usr/bin/env python
import web
import json
from cassandra.cluster import Cluster


cluster=Cluster()
#json_file=open('task.json').read()
#js = json.loads(json_file)
session = cluster.connect('list')

urls = (
    '/task','get_task',
    '/task/(.*)','get_task'


)

app = web.application(urls, globals())
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
        #js['user'].append(str(data))
        #json_file.write(js)
        print "New POST:",data
        print "json\n",js
if __name__ == "__main__":
    app.run()