from appium_test.page.base_page import BasePage
from appium_test.page.memberInvite_page import MemberInvitePage


# 通讯录页面查找添加成员
class AddressListPage(BasePage):

    def add_member(self):
        # 滚动查找元素
        self.find_by_scroll_and_click("添加成员")
        return MemberInvitePage(self.driver)
