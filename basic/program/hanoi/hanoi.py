def hanoi(n, _from, _by, _to):
    #base case
    if n==1:
        print(f'{n}번째 쟁반을 {_from}에서 {_to}로 이동 ')
        return
    
    hanoi(n-1, _from, _to, _by)
    print(f'{n}번째 쟁반을 {_from}에서 {_to}로 이동 ')
    hanoi(n-1, _by, _from ,_to)