class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        c = 0
        for ch in s:
            if ch == "I":
                ans += 1
            elif ch == "V":
                if c != 0:
                    if s[c-1] == "I":
                        ans -= 1
                        ans += 4
                    else:
                        ans += 5
                else:
                    ans += 5
            elif ch == "X":
                if c != 0:
                    if s[c-1] == "I":
                        ans -= 1
                        ans += 9
                    else:
                        ans += 10
                else:
                    ans += 10
            elif ch == "L":
                if c != 0:
                    if s[c-1] == "X":
                        ans -= 10
                        ans += 40
                    else:
                        ans += 50
                else:
                    ans += 50
            elif ch == "C":
                if c != 0:
                    if s[c-1] == "X":
                        ans -= 10
                        ans += 90
                    else:
                        ans += 100
                else:
                    ans += 100
            elif ch == "D":
                if c != 0:
                    if s[c-1] == "C":
                        ans -= 100
                        ans += 400
                    else:
                        ans += 500
                else:
                    ans += 500
            elif ch == "M":
                if c != 0:
                    if s[c-1] == "C":
                        ans -= 100
                        ans += 900
                    else:
                        ans += 1000
                else:
                    ans += 1000
            c += 1
        return ans
          