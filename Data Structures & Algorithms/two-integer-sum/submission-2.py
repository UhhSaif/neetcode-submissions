class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for i in range(1, len(nums)):
            for j in range(len(nums)):
                if i != j and (nums[j] + nums[i] == target):
                    sol.append(min(i, j))
                    sol.append(max(j, i))
                    return sol
        return sol
                