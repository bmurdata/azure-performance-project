import urllib3
from http.client import responses

http = urllib3.PoolManager()
request = http.request('GET', 'http://104.42.188.73/')

http_status = request.status
http_status_description = responses[http_status]

print(http_status)
print(http_status_description)