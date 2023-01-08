import requests

CLIENT_ID = 'dRVc9TPvKteC-ZYPo24cTA'
SECRET_KEY = 'se1wxNfU09K41dRADtIRrvFXsGCVQQ'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': 'redditrepasta',
    'password': 'ce0ad43a-7984-4661-80de-bfbccc6fad36'
}

headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'
res = requests.get('https://oauth.reddit.com/r/askreddit/hot', headers=headers)
for post in res.json()['data']['children']:
    print(post['data']['title'])
