from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.addresslist_page import AddressListPage
from appium_test.page.base_page import BasePage


# 首页-点击通讯录
class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def click_addresslist(self):
        self.find(self.addresslist_element).click()
        return AddressListPage(self.driver)
