# 13. Roman to Integer concept

The concept here is that if a current lesser chracter (ex: "I") appears before a greater character (ex: "V") then we need to subtract the current characters value. So create a hashmap to contain our characters an their values.

```python
m = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}
```

Then iterate over the string turned into an array. If the current characters map-associated value is less than the next character (if available) then subtract, else add.

```python
for i in range(len(arr)):
  if i <= len(arr)-2 and m[arr[i]] < m[arr[i+1]]:
    total = total - m[arr[i]]
  else:
    total = total + m[arr[i]]
```

Then simply return the total value

----

## Full solution

```python
class Solution:
  def romanToInt(self, s: str) -> int:
    arr = list(s)
    
    m = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    total = 0

    for i in range(len(arr)):
      if i <= len(arr)-2 and m[arr[i]] < m[arr[i+1]]:
        total = total - m[arr[i]]
      else:
        total = total + m[arr[i]]
    
    return total
```

