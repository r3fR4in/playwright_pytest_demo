import pytest
from config import setting
from playwright.sync_api import sync_playwright, Page
from page.login_page import LoginPage
import allure

USERNAME = setting.USERNAME
PASSWORD = setting.PASSWORD


@pytest.fixture(scope="class", autouse=True, name="page")
def init_browser() -> Page:
    # setupClass，初始化playwright
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        args=['--start-maximized'],
        headless=False  # 无头浏览器
    )
    context = browser.new_context(
        ignore_https_errors=True,
        no_viewport=True
    )
    page = context.new_page()
    login_page = LoginPage(page)
    with allure.step("登錄"):
        login_page.login(setting.USERNAME, setting.PASSWORD)

    yield page

    # teardownClass，关闭浏览器
    page.close()
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function", autouse=True)
def refresh_page(page):
    # 用例执行前刷新页面，就不用每次都初始化浏览器
    page.reload()
