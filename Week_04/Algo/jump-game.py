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
    def canJump(self, nums: List[int]) -> bool:
        # base case
        if 0 not in nums: return True
        if len(nums)<2: return True

        max_distance = nums[0]
        for i in range(len(nums)-1):
            if i <= max_distance:
                max_distance = max(max_distance,i+nums[i])
            else:
                break
        return max_distance >= len(nums)-1

        #时间复杂度: O(N) N为数组长度
        #空间复杂度: O(1)
print(Solution().canJump(nums=[2,3,1,1,4]))