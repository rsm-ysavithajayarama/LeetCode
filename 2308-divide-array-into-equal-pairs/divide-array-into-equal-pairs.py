class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        HashMap = Counter(nums)
        print(HashMap)
        for i in HashMap.values():
            if i%2 !=0:
                return False
            
        return True
                