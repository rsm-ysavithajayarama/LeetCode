class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = float('-inf')
        CurSum = 0
        for num in nums:
            if CurSum < 0:
                CurSum = 0
            
            CurSum += num

            if CurSum > MaxSum:
                MaxSum = CurSum
                
        return MaxSum