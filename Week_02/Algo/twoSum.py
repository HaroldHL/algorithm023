
def twoSum(nums, target):
    #首先定义一个hashMap key为值，value为索引进行保存
    hashMap = {}
    for idx, num in enumerate(nums):
        hashMap[num] = idx
    # 再循坏一次
    for i,val in enumerate(nums):
        j = hashMap.get(target - val)
        # j 不为空 且 i,j 的索引不相等
        if i != j and j is not None:
            return [i,j]

#复杂度分析
# 时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
# 空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。

print(twoSum([2,7,11,15],9))