from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


# 注意1：要先在终端链接，adb kill-server，adb connect 127.0.0.1:7555，adb devices
# 注意2：id经常变更，最好每天使用前确认一下
# 未使用po模式的企业微信添加成员功能
class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    # 企业微信添加成员作业
    def test_member(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("七月")
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/fuy").send_keys("12345685121")
        self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        # 成功案例
        mytoast = self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        # 每个页面的Toast，具备唯一性，所以可直接查找，不必担心重复
        mytoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert "添加成功" == mytoast
        # 失败案例
        # failetext = self.driver.find_element_by_xpath("//*[contains(@text,'手机已存在于通讯录')]").text
        # assert failetext == "手机已存在于通讯录，无法添加"

    # 课堂发消息练习，搜索“七月”，对“七月”发消息“测试”
    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/ie_")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gwt")
        el2.send_keys("七月")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/etm")
        el4.send_keys("测试")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/eti")
        el5.click()

    # 课堂打卡练习，外出打卡
    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        # contains：部分匹配字符串，用于难以定位的、时常变换的部分字符串，如“第N次外出”中的“次外出”
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # 获取元素的text属性
        r = self.driver.find_element_by_id("com.tencent.wework:id/pt").text
        assert "外出打卡成功" == r
