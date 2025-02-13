# Problem: A - Boy or Girl - https://codeforces.com/gym/586964/problem/A

from collections import Counter

s=input()
count=set(s)
odd=len(count)

if odd%2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
