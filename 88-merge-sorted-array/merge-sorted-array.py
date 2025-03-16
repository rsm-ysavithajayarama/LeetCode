class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = m
        R = 0
        k = 0
        while L < m+n:
            nums1[L] = nums2[R]
            L+=1
            R+=1
        nums1.sort()

            
            