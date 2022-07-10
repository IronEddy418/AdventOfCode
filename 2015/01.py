from functools import reduce


with open('./2015/01.data') as file:
    data = file.readline()
    
    function = lambda x, y: x + y
    iterable = (1 if c == '(' else -1 for c in data)
    initial_value = 0

    print(reduce(function, iterable, initial_value))
