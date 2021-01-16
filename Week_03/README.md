学习笔记

```python

# Python
def recursion(level, param1, param2, ...):     
  # recursion terminator     
  if level > MAX_LEVEL: 	   
    process_result 	   
    return     
  # process logic in current level     
  process(level, data...)     
  # drill down     
  self.recursion(level + 1, p1, ...)     
  # reverse the current level status if needed
```



### 递归要点

* 不要人肉进行递归
* 找到最近最简方法，将其拆解成可重复解决的子问题
* 数学归纳法思维

Sort():  n* logn

#### 如何计算递归算法的时间复杂度

用子问题个数乘以解决一个子问题所需要的时间





递归算法的关键要明确函数的定义，相信这个定义，而不要跳进递归细节。

写二叉树的算法题，都是基于递归框架的，我们先要搞清楚 `root` 节点它自己要做什么，然后根据题目要求选择使用前序，中序，后续的递归框架。



以下是我看到一篇博主总结的回溯算法的解题框架：

**解决一个回溯问题，实际上就是一个决策树的遍历过程**。你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。

```python

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
      	# 做选择
        将该选择从选择列表移除
        路径.add(选择)
        backtrack(路径, 选择列表)
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表
        

```

 其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」



不管怎么优化，都符合回溯框架，而且时间复杂度都不可能低于 O(N!)，因为穷举整棵决策树是无法避免的。**这也是回溯算法的一个特点，不像动态规划存在重叠子问题可以优化，回溯算法就是纯暴力穷举，复杂度一般都很高**。

