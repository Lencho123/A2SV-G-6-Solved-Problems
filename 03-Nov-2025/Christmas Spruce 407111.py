# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

class TreeNode:
    def __init__(self, val):
        self.is_leaf = True
        self.val = val
        self.children =[]

from collections import defaultdict

n = int(input())
dct = {}

for child in range(2,n+1):
    parent = int(input())
    node = TreeNode(child)
    
    if parent not in dct:
        dct[parent] = TreeNode(parent)
    dct[parent].children.append(node)
    dct[parent].is_leaf = False

res = "Yes"
for key in dct:
    leaf_count = 0
    for node in dct[key].children:
        if node.val not in dct:
            leaf_count+=1
    if leaf_count < 3:
        res = "No"
        break

print(res)
