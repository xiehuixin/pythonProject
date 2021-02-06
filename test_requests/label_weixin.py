# 企业微信实战，标签管理：
# 创建标签、更新标签名字、删除标签，使用python+requests实现
import requests


class TestLabel:

    # 在class开始前，对企业微信进行获取access_token
    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwa1792fd7bc92b4b4",
            "corpsecret": "JeS_ux7svAhS28OWrUXF8l0Gk9r3536yTO1Y-c2rPNE"}
        r = requests.request(method="GET", url=url, params=params)
        self.token = r.json()["access_token"]
        assert r.json()["errcode"] == 0

    # def test_get_tokn(self):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    #     params = {
    #         "corpid": "wwa1792fd7bc92b4b4",
    #         "corpsecret": "JeS_ux7svAhS28OWrUXF8l0Gk9r3536yTO1Y-c2rPNE"}
    #     r = requests.request(method="GET", url=url, params=params)
    #     self.token = r.json()["access_token"]
    #     assert r.json()["errcode"] == 0

    # 创建标签
    def test_create_tag(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": "UI",
            "tagid": 1
        }

        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errcode"] == 0

    # 更新标签名字
    def test_update_tag(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/" \
              f"tag/update?access_token={self.token}"
        data = {
            "tagid": 12,
            "tagname": "UI design"
        }
        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errmsg"] == "updated"

    # 删除标签
    def test_delete_tag(self):
        tagid = 1
        # 字面量插值
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        r = requests.request(method="GET", url=url)
        assert r.json()["errmsg"] == "deleted"
