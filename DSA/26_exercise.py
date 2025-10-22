def add(a, b):
    c = a + b
    print(f"sum is {c}")


add(2, 3)


def addd(*numbers):  # it will create a tuple (9,10,4)
    c = 0
    for i in numbers:
        c = c + i
    print(f"sum is {c}")


addd(10, 11, 12, 13)
