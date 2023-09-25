my_list = [1, 2, 3, 1, 2, 4, 0, 5, 2]
my_set = set()

for i in my_list:
    if my_list.count(i) > 1:
        my_set.add(i)
        
print(list(my_set))