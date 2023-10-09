# Brute Force

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ret_arr = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    ret_arr[i] = ret_arr[i] + 1
        
        return ret_arr

# Faster

class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # Deep copy
        sorted_nums = [x for x in nums]
        
        # n*log(n) sort for easier less-than-ing later
        sorted_nums.sort()

        # Hashmap for storing how many numbers are less than
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = 0
        
        # Storing highest values seen
        highest_num = sorted_nums[0]

        # Loop in the sorted nums - we know all numbers to the left are less than current index
        for i in range(len(sorted_nums)):

            # if the current number is larger
            if sorted_nums[i] > highest_num:
                # Update the highest num seen
                highest_num = sorted_nums[i]

                # Update our map with the number of nums lesser than
                dic[sorted_nums[i]] = i

        # Build our returning array
        ret_arr = [0] * len(nums)

        # Update the array with its corresponding number in the map (which is nums less than)
        for i in range(len(nums)):
            ret_arr[i] = dic[nums[i]]

        return ret_arr
