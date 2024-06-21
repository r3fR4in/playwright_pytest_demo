from config import setting
# from public.log import Log
from playwright.sync_api import Page
# 读取配置文件的URL
login_url = setting.URL
# log = Log()


class BasePage(object):
    """
    基础类，用于页面对象类的继承
    """
    def __init__(self, page: Page, base_url=login_url):
        self.base_url = base_url
        self.page = page

    def goto(self):
        url = self.base_url
        self.page.goto(url)

    # def get_by_placeholder(self, text):
    #     return self.page.get_by_placeholder(text)
    #
    # def locator(self, text):
    #     return self.page.locator(text)
