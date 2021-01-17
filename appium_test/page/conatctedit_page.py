# 可替换，因为是底层继承关系
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

from appium_test.page.base_page import BasePage


# 添加成员信息（姓名、性别、邮箱）
class ConatctEditPage(BasePage):

    def edit_name(self, name):
        name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.find(name_element).send_keys(name)
        return self

    def edit_gender(self, gender):
        self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        if gender == "女":
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        return self

    def edit_phone(self, phonenum):
        self.find((MobileBy.ID, "com.tencent.wework:id/fuy")).send_keys(phonenum)
        return self

    def cilck_save(self):
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        from appium_test.page.memberInvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
