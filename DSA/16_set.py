set_1 = {1, 2, 3, 'false', 'true'}
print(set_1)
set_1.add(99)
print(set_1)  # we can't do index slicing in it
print(len(set_1))
set_2 = {2,3,4,4,5}  # because yha per repeat huya hai so it will only consider 1-4
print(set_2)
print(len(set_2))
set_2.remove(3)
print(set_2)
set_2.add(20)
print(set_2)