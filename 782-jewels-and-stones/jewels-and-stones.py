class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mydict = {}
        res = 0
        for i in stones:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1

        for char in jewels:
            if char in mydict:
                res += mydict[char]
            
        return res if res else 0