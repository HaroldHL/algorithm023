def toLowerCase(self, str: str) -> str:
        dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'}
        res = []
        for i in str:
            if dic.get(i):
                res.append(dic[i])
            else:
                res.append(i)
        return ''.join(res)


def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1]) if s else 0


def firstUniqChar(self, s: str) -> int:
    hashMap = {}
    for idx,c in enumerate(s):
        if hashMap.get(c) is not None:
            hashMap[c] +=1
        else:
            hashMap[c] = 1
    for i in range(len(s)):
        if hashMap[s[i]] == 1:
            return i
    return -1

def numJewelsInStones(self, jewels: str, stones: str) -> int:
    hashMap ={}
    for idx,num in enumerate(stones):
        if hashMap.get(num) is not None:
            hashMap[num] +=1
        else:
            hashMap[num] = 1

    res = 0
    for i in jewels:
        if i in hashMap:
            res += hashMap[i]
    return res

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0,len(s)-1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -=1