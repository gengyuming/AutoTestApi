import requests

from TestException import MethodException


class Requests:

    def __init__(self):
        self.url = ''
        self.method = ''
        self.headers = {}
        self.body = {}
        self.files = None

    def init_request(self, url, method, headers, body, files=None):
        """
        初始化请求类
        :param url: 请求地址
        :param method: 请求方法
        :param headers: 请求头
        :param body: 请求实体
        :param files: 文件
        :return:
        """
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        self.files = files

    def send_request(self):
        """
        发送请求
        :return: 响应
        """
        if self.method.upper() == 'GET':
            response = self.__get_request__()
        elif self.method.upper() == 'POST':
            response = self.__post_request__()
        elif self.method.upper() == 'PUT':
            response = self.__put_request__()
        elif self.method.upper() == 'DELETE':
            response = self.__delete_request__()
        else:
            raise MethodException(method)

        return response

    def __get_request__(self):
        """
        GET 请求方法
        :return:
        """
        response = requests.get(url=self.url,
                                headers=self.headers,
                                params=body)


        return response

    def __post_request__(self):
        """
        POST 请求方法
        :return:
        """
        response = requests.post(url=self.url,
                                 headers=self.headers,
                                 params=self.body,
                                 files=self.files)

        return response

    def __put_request__(self):
        """
        PUT 请求方法
        :return:
        """
        response = requests.put(url=self.url,
                                headers=self.headers,
                                params=self.body,
                                files=self.files)

        return response

    def __delete_request__(self):
        """
        DELETE 请求方法
        :return:
        """
        response = requests.delete(url=self.url,
                                   headers=self.headers,
                                   params=self.body)

        return response


if __name__ == '__main__':
    url = 'https://www.jjldxz.com/api/p/bottominfo/get-city-address.json'
    method = 'POST'
    headers = {'Content-Type': 'application/json'}
    body = {'cityCode': "210200"}
    request = Requests()
    request.init_request(url=url,
                         method=method,
                         headers=headers,
                         body=body)

    response = request.send_request()
    print(response.elapsed.total_seconds())



