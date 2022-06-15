# some packages were renamed in Python 3
import urllib.request as urllib
import http.cookiejar as cookielib
import ssl

def file_get_contents(url):
    url = str(url).replace(" ", "+") # just in case, no space in url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    context = ssl._create_unverified_context()
    req = urllib.Request(url, headers=hdr)
    try:
        page = urllib.urlopen(req, context=context)
        return page.read()
    except urllib.HTTPError as e:
        print(e.fp.read())
    return ''

url = "https://api.github.com/users?since=100"
#url = "https://www.coingecko.com/en/coins/ethereum"
#request = urllib.request.Request(url)
#response = urllib.request.urlopen(request)
#data_content = response.read()
#print(data_content)
print( file_get_contents("https://twinnation.org/api/v1/ip") )
print( file_get_contents("https://www.coingecko.com/en/coins/ethereum") )