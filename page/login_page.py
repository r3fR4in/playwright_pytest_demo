from time import sleep

from page.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.pwd_login = self.page.locator('span:has-text("密碼登錄")')
        self.username = self.page.get_by_placeholder('User Name')
        self.password = self.page.get_by_placeholder('Password')
        self.login_btn = self.page.locator('button:has-text("登錄")')

    def login(self, username, password):
        self.goto()
        self.pwd_login.click()
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
        sleep(3)
