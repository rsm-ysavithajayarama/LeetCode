class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mylist = []
        for i in range(n):
            mylist.append(nums[i])
            mylist.append(nums[n+i])
        return mylist