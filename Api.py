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
        :param method:
        :return:
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
        self.body.update(param)

        return self.body

    def del_body_param(self, param: str):
        self.body.pop(param)

