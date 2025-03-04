class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counting(array):
            mydict = {}
            for i in array:
                if i in mydict:
                    mydict[i]+=1
                else:
                    mydict[i] = 1
            return mydict


        return counting(s) == counting(t)