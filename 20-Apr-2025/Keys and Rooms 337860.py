# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(key):
            visited.add(key)
            for nei in rooms[key]:
                if nei not in visited:
                    dfs(nei)
            
        dfs(0)
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True