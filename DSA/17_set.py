set_1 ={'sarthak','ram','sham'}
set_2 = {'jenny','ram', 'alakh'}
print(set_1.union(set_2))
set_1.add(99)
print(set_1)
set_1.update(['horse','mohan'])   # for adding stirngs to the set
print(set_1)
print(set_1.intersection(set_2))  # a new set is formed
print(set_1)
set_1.intersection_update(set_2)  # now set 1 is updated and is changed
print(set_1)