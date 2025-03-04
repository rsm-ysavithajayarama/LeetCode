class Solution:
    def isValid(self, s: str) -> bool:
        HashMap = { ')':'(', ']':'[', '}':'{'}
        stack = []
        
        for char in s:
            if char in HashMap:
                if stack and stack[-1] == HashMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
