# Concept - 976. Largest Perimeter Triangle

We need to return the largest perimeter. The obvious solution is to compare every set of 3 sides and then compare than some current-largest variable. But there is a much faster way. If we sort the array and reverse it to form a list from largest to smallest then we can know we are always grabing the three largest sizes that could form a triangle. Then come the triangle test where either 1 side must be less than the difference of the other two or the sum of two sides must be greater than the last side.

1. a < b - c
2. a + b > c

----

# Full Solution

```python
class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    nums = list(reversed(sorted(nums)))
    
    for i in range(len(nums) - 3 + 1):
      a = nums[i]
      b = nums[i+1]
      c = nums[i+2]

      if a + b > c and \
        a + c > b and \
        b + c > a:
        return a+b+c
    return 0
```
