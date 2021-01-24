class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Brute Force
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        # Binary Search
        size = len(nums)
        if size == 0:
            return -1

        left = 0
        right = size - 1
        while left < right:
	    #注意,这里选用的是左中位数
            mid = left + (right-left)//2
            #左半部分有序
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            #右半部分有序
            else:
		    #为了使这里left和right的更新和上面一样，所以使用nums[mid+1]
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid
        # 后处理
        return left if nums[left] == target else -1