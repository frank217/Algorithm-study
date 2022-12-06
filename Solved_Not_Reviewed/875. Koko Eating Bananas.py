#https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        # find k value. Binary search.
        # which pile to chooes Greedy.

        l,h = 1, sum(piles)

        while l < h:
            m = (l+h)//2
            hoursTaken = 0 
            #Check if its possible to complete in h hours
            for p in piles:
                hoursTaken += math.ceil(p/m)
            if hoursTaken <= hours:
                h = m
            else:
                l = m+1
        return l
