import urllib.request
import urllib.parse
import urllib.error

base = 'http://127.0.0.1:8000'
url = base + '/auth/login'
data = urllib.parse.urlencode({'username': 'test@example.com', 'password': 'test'}).encode('ascii')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

try:
    with urllib.request.urlopen(req) as resp:
        print('status', resp.status)
        print(resp.read().decode())
except urllib.error.HTTPError as e:
    print('HTTP', e.code)
    print(e.read().decode())
except urllib.error.URLError as e:
    print('URL error', e.reason)
except Exception as e:
    print('ERROR', type(e).__name__, e)
