from base.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
class LoginPage(BasePage):
    # 页面元素
    close_loc = (By.XPATH, "//i[contains(text(),'close')]")
    qiehuan_loc = (By.XPATH, "//i[contains(text(),'translate')]")
    chise_loc = (By.XPATH, "//div[contains(text(),'中文简体')]")
    denglu_loc = (By.XPATH, "//span[contains(text(),'登入')]")
    admin_loc = (By.XPATH, "//div[contains(text(),'管理员登入')]")
    username_loc = (By.XPATH, "/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/input[1]")
    password_loc = (By.XPATH, "/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/label[2]/div[1]/div[1]/div[1]/input[1]")
    submit_loc = (By.XPATH, "//body/div[3]/div[2]/div[1]/div[3]/button[1]/span[2]/span[1]")
    #断言的元素
    aman_loc = (By.XPATH,"(//button[@class='q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle text-white-8 q-btn--actionable q-focusable q-hoverable no-border-radius self-stretch q-btn-dropdown q-btn-dropdown--simple'])[1]")
    quit_loc = (By.XPATH, "//span[contains(text(),'退出登入')]")
    # 页面动作
    # def login_xuxin(self, username='Single', password='123456'):
    def login_xuxin(self,username,password):
        with allure.step("关闭注册页面："):
            self.click(LoginPage.close_loc)
        with allure.step("点击切换语言："):
            self.click(LoginPage.qiehuan_loc)
        with allure.step("点击中文简体："):
            self.click(LoginPage.chise_loc)
        with allure.step("关闭注册页面："):
            self.click(LoginPage.close_loc)
        with allure.step("点击登入："):
            self.click(LoginPage.denglu_loc)
        with allure.step("切换到管理员登录："):
            self.click(LoginPage.admin_loc)
        with allure.step("输入用户名："):
            self.set_keys(LoginPage.username_loc,username)
        with allure.step("输入密码："):
            self.set_keys(LoginPage.password_loc,password)
        with allure.step("点击登录："):
            self.click(LoginPage.submit_loc)
    #实际结果
    def get_except_result(self):
        """
        :return: 传入一个定位 返回他的值
        """
        with allure.step("点击个人中心："):
            self.click(LoginPage.aman_loc)
        with allure.step("实际结果："):
            value = self.get_value(LoginPage.quit_loc)

        return value