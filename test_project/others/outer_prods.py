import pytest
from pathlib import Path
from common.rest_client import RestClient
from common.yaml_util import YamlUtil
from common.logger import log


# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 构建配置文件路径
LOGIN_YAML_PATH = BASE_DIR / "Conf/yaml/test.yaml"
TOKEN_YAML_PATH = BASE_DIR / "Conf/yaml/token.yaml"


class TestOuterProds():
    # @pytest.mark.parametrize('caseinfo',YamlUtil(LOGIN_YAML_PATH,).read_testcase_yaml())
    # def test_get_token(self,caseinfo):
    #     """获取token"""
    #     print("DEBUG:", caseinfo)
    #     url = caseinfo['login']['url']
    #     data = caseinfo['login']['data']
    #     token = {"X-Token":RestClient().post(url,data).json()['data']['token']}
    #     log.info("正在获取token,token为：{}".format(token))
    #     YamlUtil(TOKEN_YAML_PATH).clear_extract_yaml()
    #     YamlUtil(TOKEN_YAML_PATH).write_extract_yaml(token)



    @pytest.mark.parametrize('caseinfo',YamlUtil(LOGIN_YAML_PATH,).read_testcase_yaml())
    def test_record_bill_outer(self,caseinfo):
        """上传发票"""
        url = caseinfo['record_bill_outer']['url']
        data = caseinfo['record_bill_outer']['data']
        ls = RestClient().post(url, data=data)
        print(ls)

































