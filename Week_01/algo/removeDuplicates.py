# 使用另外一个索引来判断去重，只需要循环一次
def removeDuplicates(nums):
    if not nums: return 0
    j = 0
    for i in range(len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1 

print(removeDuplicates([1,1,2]))

