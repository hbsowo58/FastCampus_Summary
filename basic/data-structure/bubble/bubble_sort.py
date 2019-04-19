def bubble_sort(li):
    n=len(li)
    flag=None
    for i in range(n-1):  #핵심은 이것
        flag = False
        for j in range(n-1-i): #두가지를 일반화 할수 있는가
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                flag = True
        if flag == False:
            break    
    return li


if __name__=="__main__":
    li=[6, 2, 1, 4]
    bubble_sort(li)
    print(li)