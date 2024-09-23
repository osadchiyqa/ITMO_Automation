# class Button:
#
#     type: str = 'Кнопка'
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
#
# # # Создаём экземпляры класса
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# # Получаем доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
#
#
# class ButtonTwo:
#
#     def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#
#     def click(self):
#         return "Клик по локатору - {}".format(self.loc)
#
#
# home_two = ButtonTwo('Домой', '/home', 'button#home')
#
# print(home_two.click())
#
#
# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# выведите в консоль значение аргумента Loc, объекта search
# class Input:
#
#     def __init__(self, loc):
#         self.loc = loc
#
# search = Input('input#search')
#
# print(search.loc)
#
#
class Input:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


search = Input('Вход', '/Расположение')
print(search.text + search.loc)


class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_1 = Button('Кнопка','/Расположение_1')

print(search_1.text + ' ' + search_1.loc)


class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_2 = Title('Заголовок','/Расположение_2')

print(search_2.text + ' -> ' + search_2.loc)


class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_3 = Link('Ссылка','/Расположение_3')

print(search_3.text + '\n' + search_3.loc)
