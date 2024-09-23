def task_1():
    a: int = 123
    b: float = 12.3
    c: str = "Hello"
    d: list = [1, 2, 3]
    e: bool = True

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

task_1()


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]

    print(a[0:3], type(a))

    print('1, 2, 3, 5, 8, 13, 21 - последовательность Фибоначчи')

task_2()


def task_3(a: int = 5) -> int:
    squared = a * a
    return squared

print(task_3())
