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

def reverseWords(s):
    #empty space
    s = s.strip()
    strs = s.split()
    strs.reverse()
    return ' '.join(strs)

def reverseWords3(s):
    return ''.join(s.split()[::-1])[::-1]


def isIsomorphic(s,t):
    hashmaps = {}
    hashmapt = {}
    for i in range(len(s)):
        if s[i] not in hashmaps: hashmaps[s[i]] = i
        if t[i] not in hashmapt: hashmapt[t[i]] = i
        
        if (hashmaps.get(s[i]) != hashmapt.get(t[i])): return False

    return True

def expandAroundCenter(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longestPalindrome(s):
    start,end = 0,0
    for i in range(len(s)):
        left1,right1 = expandAroundCenter(s,i,i)
        left2,right2 = expandAroundCenter(s,i,i+1)
    
        if right1-left1 > end-start:
            start,end = left1,right1
        if right2-left2 >end- start:
            start,end = left2,right2
    return s[start:end+1]
        
        
if __name__ == '__main__':
    print(myAtoi("42"))
    print(firstUniqChar("leetcode"))
    print(reverseWords("the sky is blue"))
    print(reverseWords3("Let's take LeetCode contest"))
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))