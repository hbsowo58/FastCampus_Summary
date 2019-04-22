def linear_search(li, target):
    for idx in range(len(li)):
        if li[idx] == target:
            return idx
    return None