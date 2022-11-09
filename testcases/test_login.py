import os

import pytest

from base.base_page import BasePage
from common.handle_path import data_path
from common.loggerController import log
from common.yaml_util import read_yaml2
from selenium import webdriver
from pageobject.login_page import LoginPage
import allure
@allure.epic('GreaterWMS 仓库管理平台')
@allure.feature('登录页面')
class TestLogin():

    @allure.severity('critical')  # 用例等级
    @allure.title('登录测试用例1')  # 测试用例标题
    @pytest.mark.parametrize("caseinfo",read_yaml2(os.path.join(data_path,'logindata.yaml')))
    def test_01_login(self,caseinfo):
        """
        lp.get_except_result()实际结果
        后面的是预期结果
        :return:
        """
        lp = LoginPage()
        lp.login_xuxin(caseinfo['username'],caseinfo['password'])
        print(lp.get_except_result())
        try:
            assert lp.get_except_result() == caseinfo['result']
        except AssertionError as e:
            log.info("断言错误")
            raise e




