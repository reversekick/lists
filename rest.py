#!/usr/bin/env python
import web
import json


json_file=open('task.json').read()
js = json.loads(json_file)

urls = (
    '/task','get_task',
    '/task/(.*)','get_task'


)

app = web.application(urls, globals())
class get_task:
    def GET(self,user):
        if len(user)==0:
            return "Usage:http://localhost:8080/task/arg1:name of user"
        ls=js['user']
        for data in ls:
            if data['name']==user:
                return str(data['task']) 
    def POST(self):
        data = web.data()
        #js['user'].append(str(data))
        #json_file.write(js)
        print "New POST:",data
        print "json\n",js
if __name__ == "__main__":
    app.run()