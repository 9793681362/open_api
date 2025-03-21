import pytest
import test_project.test_all_cases
from common.assertion_utils import ApiAssertion
from common.rest_client import RestClient
from common.yaml_util import YamlUtil
from common.logger import log

class TestAllCases():

    api_case_id = input("请输入要执行的case_id:")

    @pytest.mark.parametrize('caseinfo',YamlUtil('./Conf/yaml/test.yaml').read_yaml_excel('./api_test_case/test.xlsx','test_case'))
    def test_all_cases(self,caseinfo):
        global response
        case_id = caseinfo['payment_exception']['case_id']
        for i in [case_id]:
            if  i in self.api_case_id:
                log.info('执行的用例ID：{}'.format(case_id))
                url = caseinfo['payment_exception']['url']
                data = caseinfo['payment_exception']['data']
                is_positive = caseinfo['payment_exception']['is_positive']
                request_type = caseinfo['payment_exception']['request_type']
                expected_result = caseinfo['payment_exception']['expected_result']
                status_code = caseinfo['payment_exception']['status_code']
                field_name = caseinfo['payment_exception']['field_name']
                if request_type == "POST":
                    response = RestClient().post(url, data=data)
                    print(response.status_code)
                elif request_type == "PUT":
                    response = RestClient().put(url, data=data)
                elif request_type == "GET":
                    response = RestClient().get(url,params=data)
                print(response.json())
                assert ApiAssertion('').assert_status_code(response, status_code) == True
                log.info("状态码正确，状态码为：{}".format(response.status_code))
                if expected_result != "None":
                    assert ApiAssertion('').assert_in(response,expected_result) == True
                    log.info("断言参数返回正确，返回数据为：{}".format(response.json()))
            else:
                pytest.skip("条件不满足，跳过该测试用例")




