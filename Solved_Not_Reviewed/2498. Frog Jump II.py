# biweekly-contest-93
# https://leetcode.com/contest/biweekly-contest-93/problems/frog-jump-ii/

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # Greedy : using all the stone is always optimal solution
        # As a result of above, it doesn't matter which stone we choose, just get diff of alternating stones plus start to end.
        # The max value is our max jump
        s,e = stones[0],stones[-1]
        stones = stones[1:-1]
        l,r = [s] + stones[::2] + [e], [s] + stones[1::2] + [e]
        m,m2 = max([abs(l[i-1]-l[i]) for i in range(1,len(l))]),max([abs(r[i-1]-r[i]) for i in range(1,len(r))])
        return max(m,m2)