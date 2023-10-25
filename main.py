
def length(arr):
    count =0
    if len(arr)==0:
        return 0
    else:
        return 1+length(arr[1:])
print(length([5, 4, 3, 2, 10]))