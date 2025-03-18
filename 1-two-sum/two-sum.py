class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i,char in enumerate(nums):
            diff = target - char
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[char] = i
