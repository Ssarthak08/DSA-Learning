def second_largest():
    a = []
    for i in range(5):
        num = int(input("Enter the number"))
        a.append(num)
    print(a)
    res = a[0]

    print("There is no second largest number")
    res = a[0]
    for num in a:
        if res <= num:
            res = num
    print(f"The first largest nunmber : {res}")
    first = res
    a.remove(res)

    res_2 = a[0]
    for num in a:
        if res_2 <= num:
            res_2 = num
    print(f"The second largest number : {res_2}")
    second = res_2
    a.remove(res_2)
    if first == second:
        res_3 = a[0]
        for num in a:
            if res_3 <= num:
                res_3 = num
        print(f"Updated second largest number : {res_3}")



second_largest()
