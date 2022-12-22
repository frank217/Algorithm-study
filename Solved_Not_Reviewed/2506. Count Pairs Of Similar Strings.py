# weekly-contest-324
# https://leetcode.com/contest/weekly-contest-324/problems/count-pairs-of-similar-strings/

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = 0
        dic = defaultdict(int)
        for i in words:
            w = list(set(list(i)))
            w.sort()
            key = "".join(w)
            cnt += dic[key]
            dic[key] += 1
        return cnt

