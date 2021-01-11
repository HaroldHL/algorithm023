    def generateParenthesis(self, n: int) -> List[str]:

        def _generator(left, right, path):
            if right == n:
                res.append(path)
            if left < n:
                _generator(left+1, right, path+'(')
            if right < n and right<left:
                _generator(left, right+1, path+')')
        
        res = []
        _generator(0, 0, '')
        return res