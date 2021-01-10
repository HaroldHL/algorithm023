def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# 首先，异位词排序后应该是相同，我们用hashmap来进行保存
        hashMap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = [word]
            else:
                hashMap[sortedWord].append(word)
        # hashMap: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        # 将所有的value保存进res    
        res = []
        for value in hashMap.values():
            res.append(value)
        return res