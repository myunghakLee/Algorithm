# problem: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        def dfs(index, target):
            if index == len(nums):
                return True
            
            for i in range(len(target)): # target의 각 원소에 대해
                if target[i] == 0:
                    return False
                if target[i] >= nums[index]:
                    target[i] -= nums[index]
                    if dfs(index + 1, target):
                        return True
                    target[i] += nums[index]
                    
            return False

        total = sum(nums)
        target = [total // k] * k
        if total % k != 0 or max(nums) > target[0]:
            return False
        nums.sort(reverse=True)

        return dfs(0, target)
