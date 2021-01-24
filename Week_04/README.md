学习笔记

二分查找的模板

```python
left, right = 0,len(nums)-1
while(...):
  mid = left + (right-left)/2
  if nums[mid] == target:
    # find the target
    break or return result
  elif nums[mid]< target:
    left =...
  elif nums[mid]> target:
    right = ...
    
return ...
  
  
  
```

* 尽量不要出现else，而是把所有的情况用else if写清楚，这样可以展示所有的细节；

* mid = (left + right) / 2 在强类型的语言内可能导致**数字越界**，那么可以采用

mid = left + (right - left) / 2

* 三个前提条件
  * 1.目标函数单调性(单调递增或者递减)
  * 2.存在上下界(bounded)
  * 3.能够通过索引访问(index accessible)

