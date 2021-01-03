# 暴力 两次loop
def twoSum(nums, target):
    # res = []
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             res.append(i)
    #             res.append(j)
    # return res


# hasMap 的方法
def twoSum(nums, target):
    hasMap = {}
    for idx, num in enumerate(nums):
        hasMap[num] = idx
    for i, val in enumerate(nums):
        j = hasMap.get(target - val)
        if j is not None and i != j:
            return [i,j]

print(twoSum([2,7,11,15],9))