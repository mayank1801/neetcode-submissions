class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""
        initial_str = strs[0]
        i = 0

        for ch in initial_str:
            for str in strs[1:]:
                if i >= len(str) or ch != str[i]:
                    return ans
            ans += ch
            i += 1
        return ans

        