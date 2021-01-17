from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.base_page import BasePage
from appium_test.page.conatctedit_page import ConatctEditPage


# 点击手动输入添加
class MemberInvitePage(BasePage):
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def addconect_menual(self):
        self.find_and_click(self.addmember_element)
        return ConatctEditPage(self.driver)

    def get_toast(self):
        toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        mytoast = self.find_and_get_text(toast_element)
        return mytoast
