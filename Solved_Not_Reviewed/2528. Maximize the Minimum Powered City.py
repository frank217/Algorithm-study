# Hard 
# https://leetcode.com/contest/biweekly-contest-95/problems/maximize-the-minimum-powered-city/


from collections import deque

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # Binary Search, Moving Window, and Greedy
        
        # Check if this Max stations is possible
        def isPossible(stations,maxs,k):
            # Using Moving window to track current PowerStation
            # If Less than max stations, try adding power plant and farthest city(Greedy)
            i,n,v = 0,len(stations),sum(stations[:r])
            fix = deque()
            while i < n:
                if i-r > 0:
                    v -= stations[i-r-1]
                    while fix and fix[0][0] == i-r-1:
                        addedIndex,addedval = fix.popleft()
                        v-= addedval
                if i+r < n:
                    v += stations[i+r]
                #print(v)
                if v < maxs:
                    additional = maxs-v
                    if additional > k:
                        return False
                    addedIndex = min(i+r,n-1)
                    fix.append((addedIndex,additional))
                    k -= additional
                    v += additional
                i += 1
            return True

        # Sum of all stations + k is possible maximum number of power plant
        l,h = 0, sum(stations) + k
        # Binary Search
        while l<h:
            mid = math.ceil((l+h)/2)
            # Check if this maxium value is possible.
            if isPossible(stations,mid,k):
                l = mid
            else:
                h = mid-1
        return l