list_things = {'вода' : 4, 'еда' : 7, 'посуда' : 2, 'палатка' : 9, 'спальник' : 2, 'аптечка' : 1,
              'коврик' : 1, 'одежда' : 2}
weight_max = int(input('Максимальный вес рюкзака: '))
things = []
for i, weight in list_things.items():
    if weight <= weight_max:
        things.append(i)
        weight_max -= weight
print(things)