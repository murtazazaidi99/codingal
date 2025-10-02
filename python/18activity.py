lst=['watermellon','pineapple','grapes','apple','mango','orange','banana','cheery']
print("length of list:",len(lst))
print("firdt element:",lst[0])
print("last element:",lst[-1])

lst.append('guava')
print("updated list:",lst)

lst.remove('watermellon')
print("updated list:",lst)

lst.sort()
print("sorted list",lst)

lst.pop(1)
print("updated list:",lst)

lst.reverse()
print("reverse list:",lst)

print("multiplication on list:",lst*2)

lst=lst[0:4] 
print("sliced list:",lst)

lst.clear()
print("updated list:",lst)