def elements():
    l = []
    for i in range(5):
        num = int(input("Enter the number : "))
        l.append(num)
    print(l)
    number = int(input("Enter the element : "))
    a = []
    for i in l:
        if i <= number:
            a.append(i)
    print(a)


elements()
