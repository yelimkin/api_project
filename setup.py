# setup.py 파일이 있으면 pip로 설치가 가능하다.
from setuptools import setup

setup(
    name = "myapi", # 이 이름으로 패키지 설치
    version = "0.0.1", 
    description = "my api lib",
    url = "https://github.com/yelimkin/api_project.git",
    author = "yelimkin",
    author_email = "yelim785@gmail.com",
    packages = ["my_api"],
    install_requires = [
        "requests"
    ]
)