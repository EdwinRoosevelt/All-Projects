import urllib
from urllib import request

data = {'title' : 'Python Application Programming',
                'article_text': 'This article talks about Python and illustrates how Python is used in application programming, with examples.',
                }

data = urllib.parse.urlencode(data)
data = data.encode('ascii')

request = request.Request('http://127.0.0.1:5000/blogs/', method='POST', data=data)

try:
    response2 = request.urlopen(request)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())
