dict1 = {'one':1, 'two':2, 'three':3}
dict1.clear()
print(dict1)
dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'four':4, 'five':5}
dict1.update(dict2)
print(dict1)

dict1 = {'one': 1, 'two': 2, 'three': 3}
print(dict1.get("one"))
print(dict1.get("four", "no existe"))

print(dict1.pop("one"))
print(dict1)

dict1 = {'one': 1, 'two': 2, 'three': 3}
for value in dict1.values():
    print(value)
    
for key, value in dict1.items():
    print(key,"->",value)
    