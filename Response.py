import requests
import json
from json import JSONDecodeError


class Response:
    def __init__(self):
        self.headers = {}
        self.status_code = 0
        self.content = ''
        self.json = {}
        self.elapsed = 0

    def parse_response(self, response):
        self.headers = response.headers
        self.status_code = response.status_code
        self.content = response.content.decode('utf-8')
        try:
            self.json = json.loads(self.content)
        except JSONDecodeError as e:
            print('实体json解析失败')
        # 响应时间，单位：秒
        self.elapsed = response.elapsed.total_seconds()




