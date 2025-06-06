# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.randomSet=set()
        self.dict=defaultdict(int)
        

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False 
        self.randomSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomSet))
        # for i in self.randomSet:
        #     return i
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()