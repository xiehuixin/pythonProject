# 测试用例,使用po模式的企业微信添加成员功能
import pytest
import yaml

from appium_test.page.app import App


# 从yaml文件中读取数据
def get_data():
    with open("../data/data.yaml", encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        addnumber = data["add"]
        return addnumber


class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    # 参数化
    @pytest.mark.parametrize("name,gender,phonenum", get_data())
    def test_add_contact(self, name, gender, phonenum):
        toast = self.main.click_addresslist().add_member().addconect_menual(). \
            edit_name(name).edit_gender(gender).edit_phone(phonenum).cilck_save().get_toast()
        assert toast == "添加成功"
