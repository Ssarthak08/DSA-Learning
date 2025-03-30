def getmax():
    a = []
    for i in range(6):
        num = int(input("Enter the numbers :"))
        a.append(num)
    print(a)
    res = a[0]
    for num in a:  # Incorrect: `i` is an element, not an index
        if res <= num:
            res = num
    print(res)


getmax()

# res = a[0]
# for i in range(len(a)):  # Iterate using index values
#     if res < a[i]:  # Compare using index
#         res = a[i]
