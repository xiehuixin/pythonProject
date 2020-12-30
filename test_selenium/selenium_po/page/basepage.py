from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 基础封装
class BasePage:
    _base_url = ""

    def __init__(self, _base_url: WebDriver = None):
        # 避免driver重复初始化
        if _base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = _base_url

        if self._base_url != "":
            self.driver.get(self._base_url)

    # 元素
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 列表
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 显示等待
    def wait_for_click(self, locator, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (expected_conditions.element_to_be_clickable(locator))
        return element
