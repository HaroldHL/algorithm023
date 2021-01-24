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
    def findNum(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return nums[0]
        left,right = 0, len(nums)-1
        while left <= right: 
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[mid] < nums[mid-1]: return nums[mid]
            if nums[mid] < nums[0]: right = mid - 1
            if nums[mid] > nums[0]: left = mid + 1

print(Solution().findNum(nums=[4, 5, 6, 7, 0, 1, 2]))