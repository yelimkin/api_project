import requests
def search_api(url,client_id,client_secret,params):
    headers = {
        "X-Naver-Client-Id" : client_id,
        "X-Naver-Client-Secret" : client_secret
    }
    res = requests.get(url,params=params,headers=headers)
    result = res.json()
    if res.status_code != 200:
        print(result)
        result = None
    return result