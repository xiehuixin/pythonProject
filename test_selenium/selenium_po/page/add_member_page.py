from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.selenium_po.page.basepage import BasePage
from test_selenium.selenium_po.page.contact_page import ContactPage


# 添加成员页面
class AddMemberPage(BasePage):
    _ele_name = (By.ID, "username")
    _ele_id = (By.ID, "memberAdd_acctid")
    _ele_mail = (By.ID, "memberAdd_mail")

    # 添加成员
    def add_memebr(self, name, id, mail):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # 返回通讯录页面
        return ContactPage(self.driver)

    # 添加成员，失败案例
    def add_memebr_fail(self):
        self.driver.find_element_by_id("username").send_keys("67689")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("xx76151utuds")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("s1sa7561t1d@qq.com")
        self.driver.find_element_by_css_selector(".js_btn_save").click()
        # 返回通讯录页面
        return ContactPage(self.driver)
