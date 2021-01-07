def isAnagram(self, s: str, t: str) -> bool:
        # 暴力法
        # return sorted(s) == sorted(t)

        #An anagram that means the opposite of the original word or phrase
        # 相同的字母位置不一样 我们用一个hashMap 存放，counter
        hashMap = {}
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        # 因为异位词只是位置不一样，字母是一样的，如果是异位词，原先存放在hashmap中的值清为0
        for i in t:
            hashMap[i] -=1
        # 循环一遍 hashmap，如果没有被清空，则不是异位词
        for i in hashMap:
            if hashMap[i] != 0:
                return False
        return True

# 复杂度分析
# 都是hashMap 遍历 时间复杂度 O(N)
# 开辟新的hasMap空间 空间复杂度 O(N)