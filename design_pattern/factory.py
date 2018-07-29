"""
工厂模式
抽取项目中变化的点,使用者不用关心实现细节
"""


class ChineseGetter(object):
    def __init__(self):
        self.trans = dict(dog="狗", cat="猫")

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(language):
    languages = dict(Chinese=ChineseGetter, English=EnglishGetter)
    return languages[language]()

if __name__ == '__main__':
    c, e = get_localizer("Chinese"), get_localizer("English")
    for msg in ["dog", "bear", "fish", "cat"]:
        print(c.get(msg), e.get(msg))
