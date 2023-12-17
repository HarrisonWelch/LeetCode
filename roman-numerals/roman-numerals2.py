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