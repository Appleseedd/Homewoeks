data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def count(data_structure):
    result = 0
    if isinstance(data_structure, int):
        result += data_structure
    elif isinstance(data_structure, str):
        result += len(data_structure)
    elif isinstance(data_structure, (set, tuple, list)):
        for i in data_structure:
            result += count(i)
    elif isinstance(data_structure, dict):
        for item, resul in data_structure.items():
            result += count(item)
            result += count(resul)
    return result

print(count(data_structure))