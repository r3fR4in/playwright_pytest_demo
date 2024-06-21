import pytest
from page.goto_page import GotoPage
from page.mobile_new_page import MobileNewPage
from public.check_util import check_order_status
import allure


class TestMobileOrder:
    """流動電話服務"""

    @allure.feature("流動電話服務")
    @allure.story("新申請服務")
    @allure.title("新申請服務")
    def test_mobile_new(self, page):
        """流動電話-新申請"""
        try:
            goto_page = GotoPage(page)
            with allure.step("跳轉新申請頁面"):
                goto_page.goto_mobile_new()
            mobile_new_page = MobileNewPage(page)
            with allure.step("填寫客戶資料"):
                mobile_new_page.set_customer_information('233333')
                mobile_new_page.select_service_number()
            with allure.step("選擇產品"):
                mobile_new_page.select_product()
            with allure.step("設置sim卡"):
                mobile_new_page.set_sim_card()
                mobile_new_page.set_esim_email('test@test.com')
            with allure.step("填寫備注"):
                mobile_new_page.set_remark('teleonetest')
            with allure.step("授權"):
                mobile_new_page.authorization('csr', 'a123456')
            with allure.step("提交訂單"):
                order_number = mobile_new_page.get_order_number()
                mobile_new_page.submit_order()
            # 輪詢獲取訂單執行結果
            with allure.step("獲取訂單結果"):
                order_result = check_order_status(page, order_number)
                assert order_result
        except Exception as e:
            # 失敗或異常時截圖
            allure.attach(page.screenshot(), "失敗截圖", allure.attachment_type.PNG)
            raise e


if __name__ == '__main__':
    pytest.main(["-v", "test_mobile.py"])
