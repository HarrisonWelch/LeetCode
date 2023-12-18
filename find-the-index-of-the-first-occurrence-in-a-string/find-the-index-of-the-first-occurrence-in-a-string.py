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