from typing import Dict

thisdict: dict[str, int] = {'b': 20, 'a': 35}
print("Dictionary keys:values:", thisdict)
#negation value of b
thisdict['b'] = -20
print("Negation value of b:", thisdict)

# adding key:value in dictionary
thisdict['c'] = 45
print("Added key value:", thisdict)
# sort keys in alphabetical order
b = sorted(thisdict.keys())
print("Sorted keys:", b)

thisdict.pop('b')
print("Removed key in dictionary:", thisdict)
