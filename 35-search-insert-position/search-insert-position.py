class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        while L<=R:
            mid = (L+R)//2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return L



            