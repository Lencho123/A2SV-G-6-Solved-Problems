# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585132/problem/C

from collections import Counter

t= int(input())

for _ in range(t):
    left,right=[s for s in input().split()]
    count_l=Counter(left)
    count_r=Counter(right)
    
    if left == right:
        print("=")
    elif left[-1]==right[-1]:
        if left[-1]=="L":
            if count_l["X"] > count_r["X"]:
                print(">")
            else:
                print("<")
        else:
            if count_l["X"] > count_r["X"]:
                print("<")
            else:
                print(">")
            
    elif (left[-1]=="S" and right[-1] == "M") or (left[-1]=="S" and right[-1] == "L") or (left[-1]=="M" and right[-1] == "L"):
        print("<")
    else:
        print(">")
