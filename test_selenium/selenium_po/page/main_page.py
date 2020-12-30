from selenium.webdriver.common.by import By

from test_selenium.selenium_po.page.add_member_page import AddMemberPage
from test_selenium.selenium_po.page.basepage import BasePage
from test_selenium.selenium_po.page.contact_page import ContactPage


# 首页
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact_page(self):
        self.find(By.ID, "menu_contacts").click()
        # 进入通讯录页面
        return ContactPage(self.driver)

    def goto_add_member_page(self):
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()
        # 进入添加成员页面
        return AddMemberPage(self.driver)
