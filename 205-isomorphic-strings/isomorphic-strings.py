class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Hashmap_s = {}
        Hashmap_t = {}

        for i in range(len(s)):
            if s[i] not in Hashmap_s:
                Hashmap_s[s[i]] = i
            
            if t[i] not in Hashmap_t:
                Hashmap_t[t[i]] = i

            if Hashmap_s[s[i]] != Hashmap_t[t[i]] :
                return False
        return True