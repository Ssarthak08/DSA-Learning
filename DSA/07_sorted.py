# check if the list is sorted or not
def sorted():
    a = []
    for i in range(5):
        num = int(input("Enter the numbers : "))
        a.append(num)
    print(a)

    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            print("List is sorted ")
            break
        else:
            print("List is not sorted ")


sorted()
# let's get started
