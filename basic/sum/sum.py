def sumation(n):
    if n==1:
        return 1
    return sumation(n-1)+n
sumation(10)
sumation(10000000)


# sum =0
# num =1
# def sum(n,sum):
#     if n == 1000000:
#         print(f'합 {sum}') 내가 생각한 방식
#         return
#     elif sum += n
#          n += 1
#         sum(n,sum)
#     return
# result=sum(num,0)
# print(result)
