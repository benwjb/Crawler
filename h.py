import requests
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
resp=requests.get("http://g.91p11.space/index.php",headers=headers)
print(resp)
print(resp.text)
