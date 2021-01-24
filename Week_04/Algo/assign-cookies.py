class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 排序 + 贪心
        g.sort() #孩子数组
        s.sort() #饼干数组
        i = 0 #孩子 i
        j = 0 #饼干 j
        while i < len(g) and j < len(s):
            if g[i] <= s[j]: #能够满足一个孩子的胃口
                i += 1 #孩子饱了
            j += 1 #饼干吃了
        return i #返回被满足的孩子数

    # 时间复杂度: O(mlogm+nlogn), m,n分别是数组的长度
    # 空间复杂度: mlogm+nlogn