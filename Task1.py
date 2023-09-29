my_list = [1, 2, 3, 1, 2, 4, 0, 5, 2]
#my_set = set()
UNIO_COUNT = 1
# for i in my_list:
#     if my_list.count(i) > UNIO_COUNT:
#         my_set.add(i)
        
# print(list(my_set))
res = []
for num in my_list:
    if num not in res and my_list.count(num)> UNIO_COUNT:
        res.append(num)
print(res)