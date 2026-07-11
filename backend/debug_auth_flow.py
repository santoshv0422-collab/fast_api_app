import json
import urllib.parse
import urllib.request
import urllib.error

BASE = 'http://127.0.0.1:8000'
REGISTER_URL = BASE + '/auth/register'
LOGIN_URL = BASE + '/auth/login'
COMPANY_URL = BASE + '/company/'

user = {
    'name': 'debuguser',
    'email': 'debuguser@example.com',
    'password': 'debugpass',
    'role': 'admin'
}

headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(REGISTER_URL, data=json.dumps(user).encode('utf-8'), headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        print('REGISTER', resp.status)
        print(resp.read().decode())
except urllib.error.HTTPError as e:
    print('REGISTER HTTP', e.code)
    print(e.read().decode())
except Exception as e:
    print('REGISTER ERR', type(e).__name__, e)

login_data = urllib.parse.urlencode({'username': user['email'], 'password': user['password']}).encode('ascii')
req = urllib.request.Request(LOGIN_URL, data=login_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
try:
    with urllib.request.urlopen(req) as resp:
        print('LOGIN', resp.status)
        body = resp.read().decode()
        print(body)
        token = json.loads(body)['access_token']
except urllib.error.HTTPError as e:
    print('LOGIN HTTP', e.code)
    print(e.read().decode())
    token = None
except Exception as e:
    print('LOGIN ERR', type(e).__name__, e)
    token = None

if token:
    req = urllib.request.Request(COMPANY_URL, headers={'Authorization': f'Bearer {token}'})
    try:
        with urllib.request.urlopen(req) as resp:
            print('COMPANY', resp.status)
            print(resp.read().decode())
    except urllib.error.HTTPError as e:
        print('COMPANY HTTP', e.code)
        print(e.read().decode())
    except Exception as e:
        print('COMPANY ERR', type(e).__name__, e)
