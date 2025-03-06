class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        L,R = 0,len(s)-1
        while L<R:
            if s[L]!=s[R]:
                return False
            L+=1
            R-=1
        return True
        