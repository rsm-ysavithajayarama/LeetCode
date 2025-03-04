class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict1, mydict2 = {}, {}
        for i in s:
            if i in mydict1:
                mydict1[i] +=1
            else:
                mydict1[i] = 1
        
        for j in t:
            if j in mydict2:
                mydict2[j] +=1
            else:
                mydict2[j] = 1
        
        return mydict1 == mydict2
        