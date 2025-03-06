class Solution:
    def isPalindrome(self, x: int) -> bool:
        mystr = str(x)
        L, R = 0, len(mystr)-1
        while L < R:
            if mystr[L] != mystr[R]:
                return False
            L+=1
            R-=1
        return True
