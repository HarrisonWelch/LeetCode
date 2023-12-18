# Concept - 28. Find the Index of the First Occurrence in a String

We need to find if a string "needle" is present in a string "haystack" return the position in which the needle string appears. If it never apperas return "-1".

1. If they directly match each other, return 0.
2. Capture the size of the needle.
3. Begin iterating over the haystack to the number of characters in haystack minus the number of characters in needle. 
     * The minus is because we need an exact match - once the haystack example gets smaller than the size of the needle, we can exit.
4. Now see if needle matches the chunk of haystack we are looking at.
5. If we find a match return the iteration index. Which is the position of the haystack where we are finding a match of needle.
6. If we never found a match return -1.

----

## Full solution

```python
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if needle == haystack:
      return 0

    size = len(needle)

    for i in range(len(haystack) - size + 1):
      chunk = haystack[i:i+size]
      if chunk == needle:
        return i
    
    return -1
```
