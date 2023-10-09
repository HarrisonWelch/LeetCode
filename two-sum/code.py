## Brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

## Better solution

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2:
            return [0, 1]

        d = {}

        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d and d[comp] != i:
                return [i, d[comp]]

        return []