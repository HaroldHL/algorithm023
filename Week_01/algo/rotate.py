def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        #旋转几次就循环几次，每次把队尾的数组pop出来再insert进队首
        for i in range(k):
            lastOne = nums.pop()
            nums.insert(0,lastOne)
        return nums
print(rotate([1,2,3,4,5,6,7],3))