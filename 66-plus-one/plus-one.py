class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int(''.join([str(i) for i in digits]))
        new = str(res+1)
        return [int(i) for i in new]
        

        
        