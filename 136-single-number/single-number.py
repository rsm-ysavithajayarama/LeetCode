class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        HashMap = Counter(nums)
        for i,k in HashMap.items(): 
            if k==1:
                return i