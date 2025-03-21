# import requests
# from common.logger import log
# from common.yaml_util import YamlUtil
#
#
# class RestClient():
#     token = YamlUtil('../Conf/yaml/token.yaml').read_extract_yaml()
#
#     sess = requests.session()
#
#     def __init__(self):
#        self.session = requests.session()
#
#     def get(self,url,params,**kwargs):
#         return self.request(url,"GET",params,**kwargs,headers=self.token)
#
#     def post(self, url, data=None, json=None, **kwargs):
#        return self.request(url, "POST", data, json, **kwargs,headers=self.token)
#
#     def delete(self,url,**kwargs):
#         return self.request(url,"Delete",**kwargs,headers=self.token)
#
#     def put(self, url, data=None, json=None, **kwargs):
#         return self.request(url, "PUT", data, json, **kwargs, headers=self.token)
#
#
#
#     def request(self,url,method,data=None, json=None,params=None,**kwargs):
#         if method == "GET":
#             return requests.get(url,params,**kwargs)
#         if method == "POST":
#             return requests.post(url, data, json, **kwargs)
#         if method == "Delete":
#             return requests.delete(url,**kwargs)
#         if method == "PUT":
#             return requests.put(url, data, **kwargs)





import requests
from pathlib import Path
from common.logger import log
from common.yaml_util import YamlUtil

# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 构建 token.yaml 的路径
TOKEN_YAML_PATH = BASE_DIR / "Conf/yaml/token.yaml"

class RestClient:
    # 读取 token
    token = YamlUtil(TOKEN_YAML_PATH).read_extract_yaml()

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, **kwargs):
        return self.request(url, "GET", params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data=data, json=json, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def put(self, url, data=None, json=None, **kwargs):
        return self.request(url, "PUT", data=data, json=json, **kwargs)

    def request(self, url, method, data=None, json=None, params=None, **kwargs):
        # 添加 token 到请求头
        headers = kwargs.pop('headers', {})
        headers.update(self.token)
        print(headers)
        kwargs['headers'] = headers

        # 根据请求方法发送请求
        if method == "GET":
            return self.session.get(url, params=params, **kwargs)
        elif method == "POST":
            return self.session.post(url, data=data, json=json, **kwargs)
        elif method == "DELETE":
            return self.session.delete(url, **kwargs)
        elif method == "PUT":
            return self.session.put(url, data=data, json=json, **kwargs)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")