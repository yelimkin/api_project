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

def translate_api(text,url,client_id,client_secret,source="ko",target="en"):
    headers =  {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret" : client_secret
    }
    data = {
        "source": source, # 원본언어 코드
        "target": target, # 목적언어 코드
        "text" : text # 번역할 텍스트
    }
    res = requests.post(url,headers=headers,data=data)
    result = res.json()
    if res.status_code == 200:
        result = result["message"]["result"]["translatedText"]
    return result