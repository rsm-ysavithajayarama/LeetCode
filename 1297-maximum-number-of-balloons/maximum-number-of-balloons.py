class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter('balloon')

        res = float('inf')
        for char in balloon:
            res = min(res, countText[char]//balloon[char])
        
        return res