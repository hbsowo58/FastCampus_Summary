def binarySearch(array, value, low, high):
    if low > high:
    return False
    mid = (low+high) / 2
    if array[mid] > value:
    return binarySearch(array, value, low, mid-1)
    elif array[mid] < value:
    return binarySearch(array, value, mid+1, high)
    else:
    return mid
                        
    """
    binary_search(li, target): -> idx
    타겟을 찾았다면 인덱스를 반환
    찾지 못했다면 None을 반환
    """