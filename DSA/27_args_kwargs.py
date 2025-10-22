def add(*args):  # it will make a tuple out of it
    c = 0
    for i in args:
        c = c + i
    print(f"Total sum is {c} ")


def addd(name, *args):
    c = 0
    for i in args:
        c = c + i
    print(f"Total sum of {name} is : {c} ")


add(5, 4)
add(3, 6, 10, 7)

addd("sarthak", 3, 4, 5, 5, 6)
addd("anjor", 0, 1, 2)
