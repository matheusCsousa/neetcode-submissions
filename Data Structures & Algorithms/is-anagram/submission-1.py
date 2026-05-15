class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        eHash = {}
        for c in s:
            if c in eHash and c in t:
                eHash[c] += 1
            else:
                eHash[c] = 1
        for c in t:
            if c in eHash and c in s:
                eHash[c] += 1
            else:
                eHash[c] = 1

        for key in eHash:
            if eHash[key] % 2 == 1:
                return False 
        return True
