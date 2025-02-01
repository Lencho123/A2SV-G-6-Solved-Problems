# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    small='qwertyuiopasdfghjklzxcvbnm'
    cappital='QWERTYUIOPASDFGHJKLZXCVBNM'
    result=''
    for i in s:
        if i not in (small+cappital):
            result+=i
            continue
        
        if i in small:
            result+=i.upper()
        else:
            result+=i.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)