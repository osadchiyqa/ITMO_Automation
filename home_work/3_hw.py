def com_num(a, b):
    if a-b == 135:
        print("yes")
    else:
        print("no")

com_num(270, 136)


def year_season(season):
    if season == 12 or season == 1 or season == 2:
        print('зима')
    elif season == 3 or season == 4 or season == 5:
        print('весна')
    elif season == 6 or season == 7 or season == 8:
        print('лето')
    elif season == 9 or season == 10 or season == 11:
        print('осень')
    else:
        print('Неверно выбран месяц')

year_season(7)


def three_num(a, b, c):
    if a > 10 and b >10 and c > 10:
        print('yes')
    else:
        print('no')

three_num(10.1, 100, 11)


def sum_num(numbers):
    sum_positivs = 0
    for num in numbers:
        if num > 0:
            sum_positivs = sum_positivs + 1
        else:
            sum_positivs = sum_positivs + 0
    print(sum_positivs)

sum_num([-4, 0, 0.1, 2, 5])


def sum_days(years: int, months: int) -> int:
    if years > 0 and 1 <= months <= 12:
        days = years * months * 29
        print(days)
    else:
        print('Введите корректное значение лет или месяцев')

sum_days(5, 12.3)