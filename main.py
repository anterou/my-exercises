def sum(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        a = arr[0]
        arr.pop(0)
        return a+sum(arr)
print(sum([5, 4, 3, 2, 10]))