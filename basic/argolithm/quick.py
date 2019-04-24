def quick_sort(li, start, end):
    #base case
    #to do
    if start >= end:
        return
    
    left=start
    right=end
    pivot=li[(left+right)//2]
    
    while left <= right:
        while li[left] < pivot:
            left+=1
            
        while pivot < li[right]:
            right-=1
            
        if left <= right:
            li[left], li[right] = li[right],li[left]
            left+=1
            right-=1
    quick_sort(li, start, right)
    quick_sort(li, left, end)


    

# def quick_sort(li, start, end):
#     #base case
#     #to do
#     if start >= end:
#         return
    
#     left=start
#     right=end
#     pivot=li[(left+right)//2]
    
#     # left와 right가 교차하기 전까지
#     while left<right: 
#         #li[left]가 피벗보다 작으면
#         if li[left]<pivot:
#         #left ++
#             li[left]+1
        
#         while pivot>li[right]:
#             if li[right]>pivot:
#             #li[right]가 피벗보다 크면
#             li[right]-1
#             #right--
#         while left>right:
            
#         if left <= right:
#             li[left], li[right]=li[right], li[left]
#             left+=1
#             right-=1
            
            
            
#     quick_sort(li, start, right)
#     quick_sort(li, left, end)
            