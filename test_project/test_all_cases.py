import pytest
from common.assertion_utils import ApiAssertion
from common.rest_client import RestClient
from common.yaml_util import YamlUtil
from common.logger import log

class TestAllCases():

    @pytest.mark.parametrize('caseinfo',YamlUtil('./Conf/yaml/test.yaml').read_yaml_excel('./api_test_case/test.xlsx','test_case'))
    def test_all_cases(self,caseinfo):
        global response
        case_id = caseinfo['payment_exception']['case_id']
        url = caseinfo['payment_exception']['url']
        data = caseinfo['payment_exception']['data']
        is_positive = caseinfo['payment_exception']['is_positive']
        request_type = caseinfo['payment_exception']['request_type']
        expected_result = caseinfo['payment_exception']['expected_result']
        status_code = caseinfo['payment_exception']['status_code']
        field_name = caseinfo['payment_exception']['field_name']
        for i in [url]:
            log.info('用例ID：{}'.format(case_id))
            if request_type == "POST":
                response = RestClient().post(url, data=data)
            elif request_type == "PUT":
                response = RestClient().put(url, data=data)
            assert ApiAssertion('').assert_status_code(response,status_code) == True
            if field_name == "None":
                break
            else:
                assert ApiAssertion('').assert_response_field(response,field_name,expected_result) == True