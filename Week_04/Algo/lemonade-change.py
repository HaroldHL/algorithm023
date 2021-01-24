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
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 模拟 + 贪心
        # 5 dollars 因为柠檬树价格为5 刀，直接收下
        # 10 刀， 我们需要找5元，如果没有5元，则无法正确找零
        # 20 刀，找回15元。 有两张组合方式
            # 1张10刀 + 1张 5 刀，
            # 3张 5刀
        num5 = num10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num5 += 1
            elif bills[i] == 10:
                if num5 >= 1:
                    num5 -=1
                    num10 +=1
                else:
                    return False
            # 20 dollars
            else:
                if num5 >= 1 and num10 >= 1:
                    num10 -= 1
                    num5 -= 1
                elif num5 >= 3:
                    num5 = num5 -3
                else:
                    return False
        return True

print(Solution().lemonadeChange(bills=[5,5,5,10,20]))
print(Solution().lemonadeChange(bills=[5,5,10]))


#时间复杂度：O(N)，其中 N 是数组的长度
#空间复杂度：O(1)