"""
抽象工厂模式
写一个工厂类：参数是类名
暴露给用户是工厂类方法
只需要根据需要传入类名，调用相应的方法，就可以得到不一样的效果
求同存异
有产品族，但是只使用其中一个
"""


class ToyFactory(object):
    def __init__(self, toy_kind=None):
        self.toy_kind = toy_kind

    def show_toy(self):
        print(self.toy_kind.show())


class Thomas(object):
    @staticmethod
    def show():
        return "I'm Thomas"


class SuperMan(object):
    @staticmethod
    def show():
        return "I'm Superman"


if __name__ == '__main__':
    toy_factory = ToyFactory(SuperMan)
    toy_factory.show_toy()
