import requests
from common.logger import log

class ApiAssertion:

    def __init__(self,response):
        self.response = response

    def pass_result(self):
        self.pass_result = {
            'code': 0,
            'response_code': self.response.status_code,
            'response_reason': self.response.reason,
            'response_headers': self.response.headers,
            'response_body': self.response.text,
            'message': '测试用例执行通过',
            'check_result': True
        }

    def fail_result(self):
        self.fail_result = {
            'code': 2,
            'response_code': self.response.status_code,
            'response_reason': self.response.reason,
            'response_headers': self.response.headers,
            'response_body': self.response.text,
            'message': '测试用例断言失败，测试用例执行不通过',
            'check_result': False
        }

    def assert_status_code(self,response,expected_code):
        if response.status_code != expected_code:
            return False, f"Expected status code {expected_code}, but got {response.status_code}"
        return True

    def assert_response_field(self, response, field_name, expected_value):
        response_data = response.json()['data']
        if field_name not in response_data:
            return False, f"Response field '{field_name}' not found"
        if response_data[field_name] != expected_value:
            return False, f"Expected '{field_name}' field value '{expected_value}', but got '{response_data[field_name]}'"
        return True

    def assert_in(self,response,expected_result):
        response_data = str(response.json())
        try:
            assert str(expected_result) in response_data
            return True
        except:
            return False





    def assert_none_check(self):
        log.info("断言类型[none]——>不进行断言操作，本次断言操作通过")
        return self.pass_result


    def  assert_key_check(self,check_data):
        """
        检查json类型的响应body中是否包含一个或多个key
        :param check_data:检查数据字符串
        :return:都包含则返回Ture；有一个不包含就返回False
        """
        key_list = check_data.split(',')
        tmp_result = []
        for check_key in key_list:
            if check_key in self.response.json().keys():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
            if False in tmp_result:
                error_message = "断言类型[json_key_value]——>实际结果:%s；期望结果：%s 不相符，断言失败" % (self.response.text,check_data)
                log.error(error_message)
                self.fail_result["message"] = error_message
                return self.fail_result
            else:
                pass_message = "断言类型[json_key_value]——>实际结果：%s；期望结果：%s 相符，断言通过" % (self.response.text,check_data)
                log.info(pass_message)
                self.pass_result["message"] = pass_message
                return self.pass_result


    
















