
from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter
#输入：[5,1,1,2,0,0]
#输出：[0,0,1,1,2,5]
# bubble sort
class Solution:
    def bubble_sort(self,nums):
        for i in range(1, len(nums)):
            for j in range(0, len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    # print(Solution().bubble_sort(nums=[5,1,1,2,0,0]))
    def selection_sort(self,nums):
        for i in range(len(nums) - 1):
            # 记录最小数的索引
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            # i 不是最小数时，将 i 和最小数进行交换
            if i != minIndex:
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums
    
print(Solution().selection_sort(nums=[5,1,1,2,0,0]))           