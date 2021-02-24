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

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:    #中值 > 右值，最小值在右半边，收缩左边界     
                left = mid + 1 #因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            else:                # 明确中值 < 右值，最小值在左半边，收缩右边界               
                right = mid
        return nums[left]

print(Solution().findMin(nums=[3,4,5,1,2]))