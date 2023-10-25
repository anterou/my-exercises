def binary_search(list, item, low=0, high=None):
    if high == None:
        high = len(list)-1
    if low>high:
        return None
    else:
        mid = (low+high)//2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            return binary_search(list, item, low, mid-1)
        else:
            return binary_search(list, item, mid+1, high)
print(binary_search([1,2,3,5,12], 3))

