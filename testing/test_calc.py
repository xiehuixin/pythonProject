import pytest
# import yaml
import allure


# from python_code.calc import Calculator

# with open("./datas/calc.yaml") as f:
#     datas = yaml.safe_load(f)
#     # 加法
#     add_datas = datas['add']['datas']
#     print(add_datas)
#     add_myid = datas['add']['myid']
#     print(add_myid)
#     # 减法
#     sub_datas = datas['sub']['datas']
#     sub_myid = datas['sub']['myid']
#     # 乘法
#     mul_datas = datas['mul']['datas']
#     mul_myid = datas['mul']['myid']
#     # 除法
#     div_datas = datas['div']['datas']
#     div_myid = datas['div']['myid']


# def test_a():
#     print("python pytest 测试实战1")

@allure.feature("测试计算器")
class TestCalc:

    # def setup_class(self):
    #     print("\n开始计算")
    #     # 实例化计算器类
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("\n计算结束")

    # def setup(self):
    #     print("\n方法开始计算")
    #
    # def teardown(self):
    #     print("\n方法计算结束")

    # 加法测试
    @pytest.mark.run(order=1)
    @pytest.mark.add
    @allure.story("测试加法")
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            with allure.step("计算两个数的相加和"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 判断 result 是浮点数，作出保留2为小数的处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        finally:
            assert result == get_add_datas[2]

    # # 调用 add 方法
    # result = self.calc.add(get_add_datas[0], get_add_datas[1])
    # # 判断 result 是浮点数，作出保留2为小数的处理
    # if isinstance(result, float):
    #     result = round(result, 2)
    # # 得到结果之后，需要写断言
    # assert result == get_add_datas[2]

    # 减法测试
    @pytest.mark.run(order=2)
    @pytest.mark.sub
    @allure.story("测试减法")
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            with allure.step("计算两个数的相减"):
                result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            # 判断 result 是浮点数，作出保留2为小数的处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        finally:
            assert result == get_sub_datas[2]

    # 乘法测试
    @pytest.mark.run(order=3)
    @pytest.mark.mul
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            with allure.step("计算两个数的相乘"):
                result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            # 判断 result 是浮点数，作出保留2为小数的处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        finally:
            assert result == get_mul_datas[2]

    # 除法测试
    @pytest.mark.run(order=4)
    @pytest.mark.div
    @allure.story("测试除法")
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            with allure.step("计算两个数的相除"):
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
            # 判断 result 是浮点数，作出保留2为小数的处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        finally:
            assert result == get_div_datas[2]
