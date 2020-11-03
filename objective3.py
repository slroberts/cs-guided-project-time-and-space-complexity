"""
Constant Space O(1)
"""
def print_cspt15_n_times(n): # time complexity is O(n) Space Complexity O(1)
    for i in range(n):
        print("CSPT15")
​
"""
Linear Space O(n)
"""
def append_to_list_n_times(n):
    cspt15_list = []
​
    for _ in range(n):
        cspt15_list.append("cspt15")
​
    return cspt15_list
​
"""
Use Big O notation to classify the space complexity of the function below.
"""
def do_something(n): # Time O(n^2), Space O(n^2)
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(i + j)
​
    return lst