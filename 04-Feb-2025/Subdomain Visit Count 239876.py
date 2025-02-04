# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        def helper(s, dic):
            i=0
            arr=s.split()
            time=int(arr[0])
            domain='.'+arr[1]+'.'
            l=len(domain)

            while i<len(domain):
                if domain[i]=='.':
                    dic[domain[i+1:-1]]+=time
                i+=1
            return
        
        #work on whole cpdomains
        d=defaultdict(int)

        for element in cpdomains:
            helper(element,d)

        res=[]
        for key in d:
            if key:
                res.append(str(d[key])+' '+ key)

        return res