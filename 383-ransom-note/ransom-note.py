class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        k=0
        mylist = list(magazine)
        for i in ransomNote:
            if i in mylist:
                mylist.remove(i)
                k+=1
        return k == len(ransomNote)
