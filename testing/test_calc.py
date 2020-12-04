import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    # 加法
    add_datas = datas['add']['datas']
    print(add_datas)
    add_myid = datas['add']['myid']
    print(add_myid)
    # 减法
    sub_datas = datas['sub']['datas']
    sub_myid = datas['sub']['myid']
    # 乘法
    mul_datas = datas['mul']['datas']
    mul_myid = datas['mul']['myid']
    # 除法
    div_datas = datas['div']['datas']
    div_myid = datas['div']['myid']


def test_a():
    print("python pytest 测试实战1")


class TestCalc:

    def setup_class(self):
        print("\n开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("\n计算结束")

    def setup(self):
        print("\n方法开始计算")

    def teardown(self):
        print("\n方法计算结束")

    # 加法测试
    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=add_myid
    )
    def test_add(self, a, b, expect):
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 判断 result 是浮点数，作出保留2为小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

    # 减法测试
    @pytest.mark.parametrize(
        "a, b, expect",
        sub_datas, ids=sub_myid
    )
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 乘法测试
    @pytest.mark.parametrize(
        "a, b, expect",
        mul_datas, ids=mul_myid
    )
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 除法测试
    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas, ids=div_myid
    )
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
