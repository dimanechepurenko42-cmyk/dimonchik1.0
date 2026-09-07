data_tuple = ('h', 'c', 'e', 'T', 'k', 'e', 'e', 'G', 3, 1, 6.13, True)

Letters = [] 
Numbers = [] 

for item in data_tuple:
    if isinstance(item, str):
        Letters.append(item)
    else:
        Numbers.append(item)


Numbers.remove(6.13)     
Numbers.remove(True)
Letters.append(True)

Numbers.insert(Numbers.index(1), 2)

Numbers.sort()
Letters.reverse()

Numbers = [number ** 2 for number in Numbers]

Letters = tuple(Letters)
Numbers = tuple(Numbers)

print(Letters)
print(Numbers)