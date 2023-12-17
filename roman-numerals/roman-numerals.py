# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        arr = list(s)
        print(arr)
        total = 0
        for i in range(len(arr)):
            if arr[i] == "I":
                if i <= len(arr)-2 and arr[i+1] in ["V","X"]:
                    total = total - 1
                    continue
                total = total + 1
            if arr[i] == "V":
                total = total + 5
            if arr[i] == "X":
                if i <= len(arr)-2 and arr[i+1] in ["L","C"]:
                    total = total - 10
                    continue
                total = total + 10
            if arr[i] == "L":
                total = total + 50
            if arr[i] == "C":
                if i <= len(arr)-2 and arr[i+1] in ["D","M"]:
                    total = total - 100
                    continue
                total = total + 100
            if arr[i] == "D":
                total = total + 500
            if arr[i] == "M":
                total = total + 1000
        return total