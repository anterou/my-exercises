def most(arr):
    if len(arr)==0:
        return  0
    if len(arr)==1:
        return arr[0]
    else:
        rest_max = most(arr[1:])
        return arr[0] if arr[0]>rest_max else rest_max
print(most([2,5,12]))
