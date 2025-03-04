class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        
        for i in mydict.values():
            if i > 1:
                return True
        return False