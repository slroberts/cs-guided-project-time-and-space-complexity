def do_your_thing(items):
    last_index = len(items) - 1
    print(items[last_index])
    middle_index = len(items) // 2
    index = 0
​
    while index < middle_index:
        print(items[index])
        index = index + 1
​
    for num in range(2000):
        print(num)
​
​
def remove_duplicate(arr):
    differents = {}
​
    for i in arr:
        if i not in differents:
            differents[i] = []
            
        differents[i] += [i]
​
    return differents.keys()