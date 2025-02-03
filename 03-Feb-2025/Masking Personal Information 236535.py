# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        s=s.lower()
        res=""
        # check wether email or number

        # If email
        if "@" in s:
            arr=s.split("@")
            res=arr[0][0]+"*****"+arr[0][-1]+"@"+arr[1]
        
        # If number
        else:
            pure_number=''
            for i in s:
                if i.isdigit():
                    pure_number+=i
            
            country_code=pure_number[:-10]
            number=pure_number[-4:]

            if len(country_code)==0:
                res= "***-***-" + number
            elif len(country_code)==1:
                res= "+*-***-***-"+number
            elif len(country_code)==2:
                res= "+**-***-***-"+number
            else:
                res= "+***-***-***-"+number
        return res
