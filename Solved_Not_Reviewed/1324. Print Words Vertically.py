#https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        ans = []
        for i in range(len(s)):
            word = s[i]
            for wi in range(len(word)):
                # Need to add new row with empty space
                if wi >= len(ans):
                    ans.append("")
                # Add empty spaces 
                if len(ans[wi]) < i : 
                    ans[wi] = ans[wi] + " "*(i-len(ans[wi]))
                ans[wi] += word[wi]
        return ans