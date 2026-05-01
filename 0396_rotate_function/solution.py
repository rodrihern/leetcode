from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k+1) = F(k) - total_sum + n * nums[k]
        n = len(nums)
        res, total_sum = 0, 0
        
        # F(0)
        for i in range(n):
            total_sum += nums[i]
            res += i * nums[i]
    
        # res = max(F(k))
        current = res
        for k in range(1, n):
            current = current - total_sum + n * nums[k-1]
            res = max(res, current)

        return res
