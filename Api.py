import json


class Api:
    def __init__(self):
        self.name = ''
        self.url = ''
        self.method = ''
        self.headers = {}
        self.body = {}

    def set_name(self, name):
        self.name = name

        return self.name

    def set_url(self, url):
        self.url = url

        return self.url

    def set_method(self, method: str):
        """
        allow_method_list: ['GET', 'POST', 'PUT', 'DELETE']
        """
        self.method = method.upper()

        return self.method

    def set_headers(self, headers: dict):
        self.headers = headers

        return self.headers

    def add_header(self, header: str):
        self.headers.update(header)

        return self.headers

    def del_header(self, header: str):
        self.headers.pop(header)

        return self.headers

    def set_body(self, body: dict):
        self.body = body

        return body

    def add_body_param(self, param: dict):
        """
        :param param:
        {"param_name": {"default": "", "type": "", "range": ""}}
        default: 默认值
        type: 数据类型 --> int/float/str/list/dict
        range: 范围
        [enum1, enum2]: 枚举值
        (start, end): int --> 数值范围 / str --> 字符长度范围
        :return:
        """
        self.body.update(param)

        return self.body

    def del_body_param(self, param: str):
        self.body.pop(param)



