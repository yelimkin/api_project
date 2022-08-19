# API 프로젝트
- 설치 방법
```bash
pip install git+https://github.com/yelimkin/api_project.git
```

- 사용 방법
```python
from my_api import naver_api

search_api(url,client_id,client_secret,params)

translate_api(text,url,client_id,client_secret,source="ko",target="en")
```