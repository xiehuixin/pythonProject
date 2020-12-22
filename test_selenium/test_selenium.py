import pytest
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 获取cookie序列化后存入yaml
def test_get_cookie():
    # 调用chromeoptions方法
    opt = webdriver.ChromeOptions()
    # 设置复用浏览器的地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    # 设置隐式等待
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    with open("data.yaml", "w", encoding="utf-8") as f:
        # 快捷键导包：mac option+enter，win： alt + enter
        # 序列化cookie，存入yaml文件
        yaml.dump(cookies, f)
    driver.quit()


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 设置cookie前访问企业微信扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # 从yaml里读取cookie
    with open("data.yaml", encoding="utf-8") as f:
        yaml_datas = yaml.safe_load(f)
    for cookie in yaml_datas:
        # 把cookie传给driver
        driver.add_cookie(cookie)
    # 设置cookie后再次访问企业微信
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()

    # opt = webdriver.ChromeOptions()
    # opt.debugger_address = "127.0.0.1:9222"
    # driver = webdriver.Chrome(options=opt)
    # driver.implicitly_wait(10)
    # driver.get("https://work.weixin.qq.com/wework_admin/frame")
    # time.sleep(2)
    # driver.find_element_by_id("menu_contacts").click()

    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    # 显示等待，等待元素是可点击状态
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
    # 解决点击无效问题；设置死循环多次点击，直到目标元素出现后，跳出死循环
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id("username")
        if len(element) > 0:
            break
    # 设置输入数据
    driver.find_element_by_id("username").send_keys("test1")
    driver.find_element_by_id("memberAdd_acctid").send_keys("test1")
    driver.find_element_by_id("memberAdd_mail").send_keys("123456781@qq.com")
    driver.find_element_by_css_selector(".js_btn_save").click()
    time.sleep(1)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list = []
    for value in eles:
        # 获取元素属性title的值，存入list内
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    print()
    # 断言目标名字是否在列表内
    assert "test1" in name_list
    driver.quit()

# # 从yaml里读取cookie登录
# def test_login():
#     driver = webdriver.Chrome()
#     # 设置cookie前访问企业微信扫码登录页面
#     driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
#     # 打开yaml文件，读取cookie信息，赋值给yaml_date
#     with open("data.yaml", encoding="utf-8") as f:
#         yaml_date = yaml.safe_load(f)
#     for cookie in yaml_date:
#         # 把cookie传给driver
#         driver.add_cookie(cookie)
#     # 设置cookie后，再次访问企业微信
#     driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#     time.sleep(3)


# class TestDemo():
#     def setup_method(self, method):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#
#     def teardown_method(self, method):
#         self.driver.quit()
#
#     def test_demo(self):
#         self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
#         with open("cookie.yaml", encoding="utf-8") as f:
#             cookies = yaml.safe_load(f)
#         for cookie in cookies:
#             # 把cookie传给driver
#             self.driver.add_cookie(cookie)
#         # 设置cookie后，再次访问企业微信
#         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#         time.sleep(3)
#         # 点击 通讯录
#         self.driver.find_element_by_id("menu_contacts").click()
#         # 点击 添加成员
#         time.sleep(1)
#         self.driver.find_elements_by_xpath('//*[@class="ww_operationBar"]/a')[0].click()
#         # 姓名 输入“测试姓名”
#         self.driver.find_element_by_id("username").send_keys("测试姓名")
#         # 账号 输入“test1”
#         self.driver.find_element_by_id("memberAdd_acctid").send_keys("test1")
#         # 手机 输入“15217710462”
#         self.driver.find_element_by_id("memberAdd_phone").send_keys("15217710462")
#         # 点击 保存
#         time.sleep(1)
#         self.driver.find_elements_by_xpath('//*[@class="member_colRight_operationBar ww_operationBar"]/a')[0].click()
#         time.sleep(3)

# self.driver.get("https://www.baidu.com/")
# self.driver.find_element(By.ID, "kw").click()
# self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
# self.driver.find_element(By.ID, "su").click()
# # time.sleep(3)
# self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()
