import requests
from common.logger import log
from common.yaml_util import YamlUtil


class RestClient():
    token = YamlUtil('./Conf/yaml/token.yaml').read_extract_yaml()

    sess = requests.session()

    def __init__(self):
       self.session = requests.session()

    def get(self,url,params,**kwargs):
        return self.request(url,"GET",params,**kwargs,headers=self.token)

    def post(self, url, data=None, json=None, **kwargs):
       return self.request(url, "POST", data, json, **kwargs,headers=self.token)

    def delete(self,url,**kwargs):
        return self.request(url,"Delete",**kwargs,headers=self.token)

    def put(self, url, data=None, json=None, **kwargs):
        return self.request(url, "PUT", data, json, **kwargs, headers=self.token)



    def request(self,url,method,data=None, json=None,params=None,**kwargs):
        if method == "GET":
            return requests.get(url,params,**kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "Delete":
            return requests.delete(url,**kwargs)
        if method == "PUT":
            return requests.put(url, data, **kwargs)


