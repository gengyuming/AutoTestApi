import os
import json
from json import JSONDecodeError

import Global


class Import:
    """
    文件导入
    """
    def __init__(self):
        self.file_content = ''
        self.api_list = []

    def read_file(self, file_path):
        """
        导入格式文件
        :param file_path: 文件目录
        :return:
        """
        with open(file_path, 'r+', encoding='uft8') as file:
            self.file_content = file.read()

        api_json = self.format_content_to_json(self.file_content)
        if api_json is dict:
            self.api_list.append(api_json)
        elif api_json is list:
            for api in api_json:
                self.api_list.append(api)
        else:
            print("file content parsing type error, please debug api_json!")

        Global.API_LIST.append(self.api_list)

        return self.file_content

    @staticmethod
    def format_content_to_json(file_content):
        try:
            json_object = json.loads(file_content)
            return json_object
        except JSONDecodeError as je:
            print('import format error, please check file content!')


class Export:
    """
    文件导出
    """
    def __init__(self, ):
        self.api_list = []
        self.file_content = ''

    def save_file(self, save_path):
        path, file = save_path.rsplit('/', 1)
        if not os.path.isdir(path):
            os.makedirs(path)

        with open(save_path, 'w+', encoding='utf-8') as file:
            file.write(self.file_content)

    def format_file_content_to_str(self, api_list):
        try:
            self.api_list = api_list
            self.file_content = json.dumps(api_list, ensure_ascii=False)
            return self.file_content
        except Exception as e:
            print("Format error log: " + str(e))

