# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque

def process_chats(n, k, ids):
    screen = deque()
    seen = set()
    
    for id in ids:
        if id in seen:
            continue
        if len(screen) == k:
            removed = screen.pop()
            seen.remove(removed)
        screen.appendleft(id)
        seen.add(id)
    
    print(len(screen))
    print(' '.join(map(str, screen)))

# Example Usage:
n, k = [int(i) for i in input().split()]
ids = [int(i) for i in input().split()]
process_chats(n, k, ids)
