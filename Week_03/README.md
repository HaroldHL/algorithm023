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