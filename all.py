import pytest
import os

if __name__ == '__main__':
    # pytest.main()
    # pytest.main(['-vs','./test_project/test001_get_token.py'])
    # pytest.main(['-vs','./test_project/test_all_cases.py'])
    pytest.main(['-vs','./test_project/test_case_execution.py'])



os.system("allure generate ./reports/temp -o ./reports/html --clean")

