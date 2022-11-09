import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.handle_path import screenshots_path
from common.loggerController import log


class BasePage:

    def __init__(self):
        global driver
        # option = webdriver.ChromeOptions()
        # option.add_argument(
        #     '--user-data-dir=C:\\Users\\小杨同学\\AppData\\Local\\Google\\Chrome\\User Data\\Default')  # 加载前面获取的 个人资料路径
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.get("https://production.56yhz.com/#/web/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # yield driver
        # print("退出登陆")
        # driver.quit()
    # 定位元素
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    # 设置值的关键字
    def set_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    # 设置点击的关键字
    def click(self,loc):
        self.locator_element(loc).click()

    # 进入框架
    def goto_frame(self,frame_name):
        self.driver.switch_to_frame(frame_name)

    # 退出框架
    def quit_frame(self):
        self.driver.switch_to.default_content()

    #封装下拉框关键字
    def choice_select(self,loc,value):
        sel = Select(self.locator_element(loc,value))
        sel.select_by_value(value)

    # 获取文本的值
    def get_value(self,loc):
        return self.locator_element(loc).text

    # 截图
    def save_webImgs(self, model=None):
        # filepath = 指图片保存目录/model(页面功能名称)_当前时间到秒.png
        # 截图保存目录
        # 拼接日志文件夹，如果不存在则自动创建
        cur_path = os.path.dirname(os.path.realpath(__file__))
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # os.path.join((screenshots_path), f'screenshots\\{now_date}')

        screenshot_path = os.path.join(os.path.dirname(cur_path), f'creenshots\\{now_date}')
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
        # 当前时间
        dateNow = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        # 路径
        filePath = '{}\\{}_{}.png'.format(screenshot_path, model, dateNow)
        try:
            self.driver.save_screenshot(filePath)
            log.info(f"截屏成功,图片路径为{filePath}")
        except:
            log.exception('截屏失败!')


