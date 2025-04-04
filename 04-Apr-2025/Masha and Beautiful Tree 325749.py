# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right): 
        global swap       
        if left[0] > right[0]:
            swap+=1
            return right + left
        else:
            return left + right
    
    swap = 0
    
    if mergeSort(arr) == sorted(arr):
        print(swap)
    else:
        print(-1)
