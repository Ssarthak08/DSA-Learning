numbers = [101, 11, 12, 100, 1000, 121, 113]
names = ['sarthak', 'devansh']
print(names)
print(numbers)
print(numbers[1])
print(numbers[0:6:2])   # 6 not included, uptill 6
numbers.sort()  # it's a function and returns nothing
numbers.reverse()
print(numbers)
numbers.append(45)  # it only takes one argument
print(numbers)
numbers.append(20)  # it only takes one argument and that too at very end
print(numbers)
numbers.insert(2, 45)  # it takes 2 arguments
numbers.insert(0,33)
print(numbers)
numbers.extend([12, 13, 14, 15])  # needs to be in a list form
print(numbers)
numbers.remove(101)
print(numbers)
print(numbers.pop(3))   # pooped index 3
print(numbers)
print(len(numbers))
