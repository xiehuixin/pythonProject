# 类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
import yaml


class Animal:
    name: str = None
    color: str = None
    age: int = 0
    gender: str = None

    def canCall(self):
        print("can call")

    def canRan(self):
        print("can ran")

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender


# 创建子类【猫】，继承【动物类】，
# 复写父类的__init__方法，继承父类的属性，
# 添加一个新的属性，毛发=短毛，
# 添加一个新的方法， 会捉老鼠，
# 复写父类的‘【会叫】的方法，改成【喵喵叫】

class Cat(Animal):
    hair: str = None

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def canCall(self):
        print("喵喵叫")

    def canDo(self):
        print("会捉老鼠")


# 创建子类【狗】，继承【动物类】，
# 复写父类的__init__方法，继承父类的属性，
# 添加一个新的属性，毛发=长毛，
# 添加一个新的方法， 会看家，
# 复写父类的【会叫】的方法，改成【汪汪叫】

class Dog(Animal):
    hair: str = None

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def canCall(self):
        print("汪汪叫")

    def canDo(self):
        print("会看家")


# 调用 name== ‘main’：
# 创建一个猫猫实例
# 调用捉老鼠的方法
# 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
# 创建一个狗狗实例
# 调用【会看家】的方法
# 打印【狗狗的姓名，颜色，年龄，性别，毛发】。


# cat = Cat("短毛","猫猫","黑",1,"女")
# print(cat.name)
# print(cat.color)
# print(cat.age)
# print(cat.gender)
# print(cat.hair)
# cat.canDo()
# cat.canCall()

if __name__ == '__main__':
    with open("Animal.yaml", encoding="UTF-8") as f:
        animals = yaml.safe_load(f)

    # print(animals['cat'])
    cat = animals['cat']
    cat1 = Cat(cat['hair'], cat['name'], cat['color'], cat['age'], cat['gender'])
    print(f"猫猫的姓名:{cat1.name},颜色:{cat1.color}，年龄：{cat1.age}，性别:{cat1.gender}，毛发:{cat1.hair}")
    cat1.canDo()
    print()

    dog = animals['dog']
    dog1 = Dog(dog['hair'], dog['name'], dog['color'], dog['age'], dog['gender'])
    dog1.canDo()
    print(f"狗狗的姓名:{dog1.name},颜色:{dog1.color}，年龄：{dog1.age}，性别:{dog1.gender}，毛发:{dog1.hair}")
    dog1.canCall()
