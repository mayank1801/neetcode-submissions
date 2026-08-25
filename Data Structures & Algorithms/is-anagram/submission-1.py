class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        visit = [0] * 26

        for i in range(len(s)):
            visit[ord(s[i]) - ord('a')] += 1
            visit[ord(t[i]) - ord('a')] -= 1

        for k in visit:
            if k != 0:
                return False
        return True       