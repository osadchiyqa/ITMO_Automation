from task_9_checks import Checks
class Input(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


search = Input('Вход', '/Расположение')
print(search.text)
print(search.check_text())


class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_1 = Button('Кнопка','/Расположение_1')

print(search_1.text)
print(search_1.check_text())


class Title(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_2 = Title('Заголовок','/Расположение_2')

print(search_2.text)
print(search_2.check_text())


class Link(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_3 = Link('Ссылка','/Расположение_3')

print(search_3.text)
print(search_3.check_text())