class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, char in enumerate(nums):
            diff = target - char
            if diff in mydict:
                return [mydict[diff], i]
            mydict[char] = i
