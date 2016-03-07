import requests

r = requests.post("http://localhost:8080/task",json={"name":"mustafa","id":8,"title":"go for business","priority":3,"creationTime":"10","endTime":24,"status":"incomplete","postponeCount":1})
print(r.status_code, r.reason)