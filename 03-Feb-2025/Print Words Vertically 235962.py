# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr=s.split(' ')

        arr_len=[len(n) for n in arr]
        mx_len=max(arr_len)
        l=len(arr)
        res=[]
        
        print(arr, arr_len, mx_len)
        for i in range(mx_len):
            cur=''
            for j in range(l):
                if i<arr_len[j]:
                    cur+=arr[j][i]
                else:
                    cur+=' '
            res.append(cur)

            # clean up the trailing spaces

            output=[]
            for i in res:
                j=len(i)-1
                while j>=0 and i[j]==' ':
                    j-=1
                output.append(i[:j+1])
                    
        return output