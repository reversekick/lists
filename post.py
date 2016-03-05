import requests

r = requests.post("http://localhost:8080/task", json={"name":"Mustafa","task":[{"id":5,"title":"Start a business","startTime":10,"endTime":2}]})

print(r.status_code, r.reason)