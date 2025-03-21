import pytest
from pathlib import Path
from common.rest_client import RestClient
from common.yaml_util import YamlUtil
from common.logger import log


# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# 构建配置文件路径
LOGIN_YAML_PATH = BASE_DIR / "Conf/yaml/test.yaml"
TOKEN_YAML_PATH = BASE_DIR / "Conf/yaml/token.yaml"


class TestOuterProds():

    @pytest.mark.parametrize('caseinfo',YamlUtil(LOGIN_YAML_PATH,).read_testcase_yaml())
    def test_new_product(self,caseinfo):
        """上传发票"""
        url = caseinfo['new_product']['url']
        print(url)
        data = caseinfo['new_product']['data']
        print(data)
        ls = RestClient().post(url, data=data)
        print(ls)
        print(ls.status_code)
        print(ls.text)



class TestOuterProds2():

    @pytest.mark.parametrize('caseinfo',YamlUtil(LOGIN_YAML_PATH,).read_testcase_yaml())
    def test_new_product2(self,caseinfo):
        """上传发票"""
        url = caseinfo['new_product2']['url']
        print(url)
        data = caseinfo['new_product2']['data']
        print(data)
        ls = RestClient().get(url,params=data)
        print(ls)
        print(ls.status_code)
        print(ls.text)

