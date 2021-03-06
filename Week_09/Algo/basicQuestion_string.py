def toLowerCase(str):
        dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'}

        res = []
        for ch in str:
            if ch in dic:
                res.append(dic[ch])
            else:
                res.append(ch)
        return ''.join(res)

def numJewelsInStones(jewels,stones):
        hashMap = {}
        for c in stones:
            if hashMap.get(c) is not None:
                hashMap[c] +=1
            else:
                hashMap[c] =1
        res=0
        for c in jewels:
            if c in hashMap:
                res += hashMap[c]
        return res

def reverseOnlyLetters(S):
        stack = []
        res = []
        for c in S:
            if c.isalpha():
                stack.append(c)
        for c in S:
            if c.isalpha():
                res.append(stack.pop())
            else:
                res.append(c)
        return "".join(res)

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

def validPalindrome2(s):
        def isPalindrome(i,j):
            while i <j:
                if s[i] != s[j]:
                    return False
                i +=1
                j -=1
            return True
        i,j = 0,len(s)-1
        while i <j:
            if s[i] != s[j]:
                return isPalindrome(i+1, j) or isPalindrome(i, j-1)
            i +=1
            j -=1
        return True
    
if __name__=='__main__':
    str1 = 'Hello'
    print(toLowerCase(str1))
    print(numJewelsInStones("aA","aAAbbbb"))
    print(firstUniqChar("loveleetcode"))
    print(reverseOnlyLetters("ab-cd"))