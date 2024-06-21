from page.base_page import BasePage


class GotoPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.close = self.page.locator('xpath=//html/body/div[4]/div[2]/div/div[1]/i')
        self.home = self.page.locator('span:has-text("HOME")')
        self.csms = self.page.locator('span:has-text("CSMS")')
        self.biz_processing = self.page.locator('li').filter(has=self.page.get_by_text("業務辦理", exact=True))
        self.mobile = self.biz_processing.locator('li').filter(has_text='流動電話服務')
        # 流動電話新申請
        self.mobile_new = self.mobile.locator('span:has-text("新申請服務")')

    def goto_mobile_new(self):
        # self.close.click()
        self.home.click()
        self.csms.click()
        self.biz_processing.click()
        self.mobile.click()
        self.mobile_new.click()
