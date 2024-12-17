class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs)
        if len(strs[0]) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        for ch in strs[0]:
            ans += ch
            for string in strs:
                ans2 = ""
                for ch2 in string:
                    ans2 += ch2
                    if len(ans2) == len(ans):
                        break
                if ans2 == ans:
                    continue
                else:
                    li = list(ans)
                    li.pop()
                    ans = ''.join(li)
                    return ans
        return ans