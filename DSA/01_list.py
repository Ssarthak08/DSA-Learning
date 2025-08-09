# taking input as a list from the user and find its average
def average(l):
    sum = 0
    count = 0
    for i in l:
        sum = sum + i
        count = count + 1
    total_average = sum / count
    print(total_average)


l = [10, 20, 30, 40]
average(l)  # update
