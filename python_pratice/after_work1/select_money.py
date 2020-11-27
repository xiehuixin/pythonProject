# 工资查询模块 select_money，用来展示工资数额
import money


def select_money():
    if money.saved_money == 1000:
        print("还没发工资")
    else:
        print(f"工资数额{money.saved_money}")
