class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base case
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = collections.deque()
        visited= set()
        n = len(beginWord)

        queue.append((beginWord,1))
        while queue:
            cur,step = queue.popleft()
            if cur == endWord:
                return step

            for i in range(n):
                for j in range(26):
                    temp = cur[:i]+ chr(97+j) +cur[i+1:]
                    if temp not in visited and temp in word_set:
                        queue.append((temp,step+1))
                        visited.add(temp)
        return 0