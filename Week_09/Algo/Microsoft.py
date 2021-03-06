def myAtoi(s):
    #Empty String
    if len(s) ==0: return 0

    #remove space    
    ls = list(s.strip())
    if len(ls) == 0:return 0
    print(ls)
    #hanle signs
    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-','+']: del ls[0]
    res,i =0,0
    while i < len(ls) and ls[i].isdigit():
        res = res*10 + ord(ls[i]) - ord('0')
        i +=1
    return max(-2**31, min(sign * res,2**31-1))

def firstUniqChar(s):
    hashMap = {}
    for ch in s:
        if hashMap.get(ch) is not None:
            hashMap[ch] +=1
        else:
            hashMap[ch] = 1
    for i in range(len(s)):
        if hashMap.get(s[i]) == 1:
            return i
    return -1
    
    
if __name__ == '__main__':
    s = "42"
    print(myAtoi(s))
    str1 = "leetcode"
    print(firstUniqChar(str1))