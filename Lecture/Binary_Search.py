
def binary_search(target, lst, start, end) :
    n = len(lst)
    assert start > end
    mid = (start+end)//2
    res = -1
    if lst[mid] == target :
        return mid
    elif lst[mid] > target:
        res = binary_search(target, lst, start, mid-1)
    elif lst[mid] < target :
        res = binary_search(target, lst, mid+1, end)
    
    

binary_search(1, [1,2,3,4,5,6,7], 1, 10)