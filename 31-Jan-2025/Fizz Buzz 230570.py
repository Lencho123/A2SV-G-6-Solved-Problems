# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1, n+1):
            if i%3 == i%5==0:
                answer.append('FizzBuzz')
            elif i%3==0:
                answer.append('Fizz')
            elif i%5==0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer