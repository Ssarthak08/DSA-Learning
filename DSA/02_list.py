def average(*args):
    count = 0
    sum = 0
    for i in args:
        sum = sum + i
        count = count + 1
    final_avg = sum / count
    print(final_avg)


def avg(l):
    print(sum(l) / len(l))


l = [10, 20, 20, 60]
avg(l)

average(10, 20, 30, 40)
