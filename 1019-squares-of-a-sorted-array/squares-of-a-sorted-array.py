class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        L, R = 0, len(nums)-1
        mylist = []
        while L <=R:
            if nums[L]**2 > nums[R]**2:
                mylist.append(nums[L]**2)
                L+=1
            else:
                mylist.append(nums[R]**2)
                R-=1
        
        return mylist[::-1]

