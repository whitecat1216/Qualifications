import urllib.request
import urllib.parse

data=urllib.parse.urlencode({"key":"value"}).encode("utf-8")
req=urllib.request.Request("http://example.com", data=data,method="POST")
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))  # サーバーからのレスポ