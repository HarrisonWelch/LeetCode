class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxP = 0
        nums = sorted(nums)
        for i in range(len(nums) - 3 + 1):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]

            print(a,b,c)

            if a + b > c and \
                a + c > b and \
                b + c > a:
                if a + b + c > maxP:
                    maxP = a + b + c
        return maxP