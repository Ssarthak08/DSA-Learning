# else will only be executed if for block has completely been finished
numbers = [1, 2, 3, 43, 5]
for i in numbers:
    print(i)
    if i == 43:
        break
else:
    print("printed all numbers ")

