def hanoi(n,start,temp,end):
    if n==1:
        print("Move Disk 1 from rod",start,"to rod",end)
        return
    hanoi(n-1,start,temp,end)
    print("Move Disk",n," From rod",start,"to rod",end)
    hanoi(n-1,temp,start,end)
n=int(input())
hanoi(n,'A','B','C')
