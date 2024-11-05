import pytest
from common.rest_client import RestClient
from common.yaml_util import YamlUtil
from common.logger import log


class Test_login():
    @pytest.mark.parametrize('caseinfo',YamlUtil('../Conf/yaml/login.yaml').read_testcase_yaml())
    def test_get_token(self,caseinfo):
        """获取token"""
        url = caseinfo['login']['url']
        data = caseinfo['login']['data']
        token = {"X-Token":RestClient().post(url,data).json()['data']['token']}
        log.info("正在获取token,token为：{}".format(token))
        YamlUtil('./Conf/yaml/token.yaml').clear_extract_yaml()
        YamlUtil('./Conf/yaml/token.yaml').write_extract_yaml(token)

