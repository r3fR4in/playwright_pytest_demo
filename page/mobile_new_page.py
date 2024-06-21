import re
from time import sleep

from page.base_page import BasePage


class MobileNewPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.order_number_area = self.page.locator("xpath=//*[@id=\"app\"]/div/header/div[1]/h4")

        self.id_number_type_select = self.page.locator('xpath=//*[@id="queryCustomerInfoNew"]/section/form/div[2]/div/div/div/div[1]/div/div/input')
        self.id_AA_Austria = self.page.get_by_role("listitem").filter(has_text='ID-AA-Austria')
        self.id_number_input = self.page.get_by_placeholder('請輸入證件號碼')
        self.search_btn = self.page.locator('xpath=//*[@id="queryCustomerInfoNew"]/section/form/div[2]/div/div/div/div[2]/button')
        self.use_btn = self.page.get_by_role("button").filter(has_text='使用').nth(0)
        self.confirm_btn1 = self.page.get_by_role("dialog", name="提示").get_by_role("button", name="確認")
        self.exempt_government_approval_check = self.page.locator("#comCustomerInfo").locator('div').filter(has=self.page.get_by_role("checkbox"))
        self.reason_for_exemption_select = self.page.locator("#comCustomerInfo input[name=\"categoryCode\"]")
        self.reason_for_exemption = self.page.get_by_role("listitem").filter(has_text='中國內地、香港、澳門身份證及藍卡無需審批')

        self.service_number_type_select = self.page.locator("#selectServiceNumber input").nth(0)
        self.ctm_hq = self.page.get_by_role("listitem").filter(has_text='CTM HQ')
        self.select_service_number_btn = self.page.locator('button:has-text(" 客戶選號")')
        self.service_number = self.page.get_by_role("dialog", name="選擇號碼").locator("div[class=\"select_dialog\"] div div").nth(0)
        self.confirm_btn2 = self.page.get_by_role("dialog", name="選擇號碼").get_by_role("button", name="確認")

        self.select_product_area = self.page.locator("#selectProduct")
        self.select_product_btn = self.select_product_area.locator('button:has-text(" 選擇產品/服務 ")')
        self.select_product_dialog = self.page.get_by_role("dialog", name="選擇產品/服務")
        self.service_tab = self.select_product_dialog.get_by_role("tab", name="服務", exact=True)
        self.service_type = self.select_product_dialog.get_by_placeholder("服務類型")
        self.po = self.page.get_by_role("listitem").filter(has=self.page.get_by_text("PO", exact=True))
        self.add_btn = self.select_product_dialog.locator("#pane-offer div[class=\"cell\"] i").nth(2)
        self.selected_service_tab = self.select_product_dialog.get_by_role("tab", name="已選服務總覽", exact=True)
        self.confirm_btn3 = self.select_product_dialog.get_by_role("button", name="確認")

        self.sim_card_info_area = self.page.locator("#simCardInfo")
        self.eSIM = self.sim_card_info_area.get_by_role("radio").nth(1)
        self.get_eSIM_btn = self.sim_card_info_area.get_by_role("button", name="獲取")
        self.confirm_btn4 = self.page.get_by_role("dialog", name="提示").get_by_role("button", name="確認")
        self.reserve_btn = self.sim_card_info_area.get_by_role("button", name="預留")
        self.confirm_btn5 = self.sim_card_info_area.get_by_role("dialog", name="提示").get_by_role("button", name="確認")

        self.esim_area = self.page.locator("#prepaidEsim")
        self.esim_email = self.esim_area.get_by_placeholder("請輸入Email")

        self.remark_info_area = self.page.locator("#remarksInfo")
        # self.remark_input = self.remark_info_area.locator("textbox:right-of(label:has-text(\"備注\"))")
        self.remark_input = self.remark_info_area.locator("textarea")

        self.id_card_register_area = self.page.locator("#idCardRegister")
        self.authorization_btn = self.id_card_register_area.get_by_role("button", name="授權")
        self.username_input = self.id_card_register_area.get_by_role("dialog", name="授權").get_by_placeholder("請輸入用戶名")
        self.password_input = self.id_card_register_area.get_by_role("dialog", name="授權").get_by_placeholder("請輸入密碼")
        self.confirm_btn6 = self.id_card_register_area.get_by_role("dialog", name="授權").get_by_role("button", name="確定")

        self.submit_btn = self.page.get_by_role("button", name="提交")
        self.confirm_btn7 = self.page.get_by_role("dialog", name="提示").get_by_role("button", name="確定")
        self.confirm_btn8 = self.page.locator("xpath=//*[@id=\"app\"]/div/div[6]/div[1]/div/div[3]/button")

    """獲取訂單號"""
    def get_order_number(self):
        s = self.order_number_area.inner_text()
        order_number = ''.join(re.findall(r'\d+', s))

        return order_number

    """設置客戶資料"""
    def set_customer_information(self, id_number):
        self.id_number_type_select.click()
        self.id_AA_Austria.click()
        self.id_number_input.fill(id_number)
        self.search_btn.click()
        self.use_btn.click()
        self.confirm_btn1.click()
        self.exempt_government_approval_check.click()
        self.reason_for_exemption_select.click()
        self.reason_for_exemption.click()

    """選擇服務號碼"""
    def select_service_number(self):
        self.service_number_type_select.click()
        self.ctm_hq.click()
        self.select_service_number_btn.click()
        self.service_number.click()
        self.confirm_btn2.click()

    """選擇產品/服務"""
    def select_product(self):
        self.select_product_btn.click()
        self.service_tab.click()
        self.service_type.click()
        self.po.click()
        sleep(1)
        self.add_btn.click()
        self.selected_service_tab.click()
        self.confirm_btn3.click()

    """設置sim卡"""
    def set_sim_card(self):
        self.eSIM.click()
        self.get_eSIM_btn.click()
        self.confirm_btn4.click()
        self.reserve_btn.click()
        self.confirm_btn4.click()
        self.confirm_btn5.click()

    """設置esim的email"""
    def set_esim_email(self, email):
        self.esim_email.fill(email)

    """設置備注"""
    def set_remark(self, remark):
        self.remark_input.fill(remark)

    """授權"""
    def authorization(self, username, password):
        self.authorization_btn.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_btn6.click()

    """提交訂單"""
    def submit_order(self):
        self.submit_btn.click()
        self.confirm_btn7.click()
        self.confirm_btn8.click()
