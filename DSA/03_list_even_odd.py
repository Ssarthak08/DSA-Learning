# separating even and odd from the given list
def separate(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)


l = [1, 2, 10, 11, 22, 23, 33, 34]
separate(l)
