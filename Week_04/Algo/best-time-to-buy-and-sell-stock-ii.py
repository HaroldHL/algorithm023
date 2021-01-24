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
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        # 遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）
        # 设 tmp 为第 i-1 日买入与第 i 日卖出赚取的利润，即 tmp = prices[i] - prices[i - 1]
        # 设 tmp 为第 i-1 日买入与第 i 日卖出赚取的利润，即 tmp = prices[i] - prices[i - 1]
        profit = 0
        for i in range(1,len(prices)):
            temp = prices[i] - prices[i-1]
            if temp > 0:
                profit += prices[i] - prices[i-1]
        return profit

        # 时间复杂度 O(N)
        # 空间复杂度 O(1) 变量使用常数额外空间
print(Solution().maxProfit(prices=[7,1,5,3,6,4]))