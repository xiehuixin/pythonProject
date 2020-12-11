from typing import List

import pytest
import yaml
import os
from python_code.calc import Calculator

# 获取 yaml 文件所在的绝对路径
yaml_file_path = os.path.dirname(__file__) + "/datas/calc.yaml"

with open(yaml_file_path, encoding="UTF-8") as f:
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


# 加法
@pytest.fixture(params=add_datas, ids=add_myid)
def get_add_datas(request):
    print("\n开始计算")
    data = request.param
    # print(f"request.param 里面的测试数据是：{data}")
    yield data
    print("\n结束计算")


# 减法
@pytest.fixture(params=sub_datas, ids=sub_myid)
def get_sub_datas(request):
    print("\n开始计算")
    data = request.param
    # print(f"request.param 里面的测试数据是：{data}")
    yield data
    print("\n结束计算")


# 乘法
@pytest.fixture(params=mul_datas, ids=mul_myid)
def get_mul_datas(request):
    print("\n开始计算")
    data = request.param
    # print(f"request.param 里面的测试数据是：{data}")
    yield data
    print("\n结束计算")


# 除法
@pytest.fixture(params=div_datas, ids=div_myid)
def get_div_datas(request):
    print("\n开始计算")
    data = request.param
    # print(f"request.param 里面的测试数据是：{data}")
    yield data
    print("\n结束计算")


@pytest.fixture(scope='session')
def connectDB():
    print("\n连接数据库操作")
    yield
    print("\n断开数据库连接")


@pytest.fixture(scope="class")
def get_calc():
    print("\n获取计算器实例")
    calc = Calculator()
    return calc


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.
    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    # print("items")
    # print(items)
    # 实现用例反转执行
    # items.reverse()

    # 修改测试用例参数编码格式
    for item in items:
        item.name = item.name.encode("UTF-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("UTF-8").decode("unicode-escape")

        # item.nodeid 拿到的是测试用例的名称
        # 自动给测试用例加上标签
        # if 'add' in item.nodeid:
        #     item.add_marker(pytest.mark.add)
        # elif 'div' in item.nodeid:
        #     item.add_marker(pytest.mark.div)
        # elif 'sub' in item.nodeid:
        #     item.add_marker(pytest.mark.sub)
        # elif 'mul' in item.nodeid:
        #     item.add_marker(pytest.mark.mul)
