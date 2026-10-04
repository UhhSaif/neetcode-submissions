class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        longest = 1
        count = 1
        for n in range(1, len(nums)):
            if nums[n-1] == nums[n]:
                continue
            if nums[n-1] == nums[n] - 1:
                count += 1
            else: 
                count = 1

            longest = max(longest, count) 
                
        return longest
                
        
        