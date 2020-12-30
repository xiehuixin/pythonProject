import pytest

from test_selenium.selenium_po.page.main_page import MainPage


# 测试用例编写
class TestLogin:

    # 进入首页
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,mail", [("wangwu", "wangwu", "wangwu@qq.cm")])
    def test_login(self, name, id, mail):
        # name = "zhangsan"
        # id = "asdfas1"
        # mail = "asdqweq@qq.com"
        # 首页-通讯录-添加成员-断言
        namelist = self.main.goto_contact_page().click_add_member(). \
            add_memebr(name, id, mail).get_member()
        print(namelist)
        # 断言
        assert name in namelist

    @pytest.mark.parametrize("name,id,mail", [("zhangsan", "zhangsan", "zhangsan@qq.cm")])
    def test_login1(self, name, id, mail):
        # name = "zhangsan"
        # id = "asdfas1"
        # mail = "asdqweq@qq.com"
        # 首页-添加成员-断言
        namelist = self.main.goto_add_member_page(). \
            add_memebr(name, id, mail).get_member()
        print(namelist)
        # 断言
        assert name in namelist
