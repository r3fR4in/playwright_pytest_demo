import pytest
from datetime import datetime

if __name__ == '__main__':
    # allure serve report目录，启动服务查看报告
    # allure generate report目录，生成html文件报告
    current_time = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    pytest.main(["-s", "-v", "-n 2", "--dist=loadscope", "--alluredir=./report/{}".format(str(current_time))])
    # pytest.main(["-v", "testcase/test_mobile.py"])
    # pytest.main(["-v", "testcase/test_internet.py"])
