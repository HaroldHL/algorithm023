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
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtrack(path,select):
            # 如果路径不在结果集中
            if not select and path not in res:
                res.append(path[:])
                return 
            
            for i in range(len(select)):
                # 添加路径
                path.append(select[i])
                # drill down 更新选择列表不存在path的选择列表
                backtrack(path,select[:i]+select[i+1:])
                # 取消选择
                path.pop()

        backtrack([],nums)
        return res

print(Solution().permute(nums=[1,1,2]))