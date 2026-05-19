class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        tMap = {}
        res = ""
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        have = 0
        need = len(tMap)

        start = 0
        for end in range(len(s)):
            char = s[end]
            if char in tMap:
                window[char] = window.get(char, 0) + 1
                if window[char] == tMap[char]:
                    have += 1
                
            while have == need:
                if not res or (end - start + 1) < len(res):
                    res = s[start:end+1]
                
                left_char = s[start]
                if left_char in tMap:
                    window[left_char] -= 1
                    if window[left_char] < tMap[left_char]:
                        have -= 1
                start += 1
        return res