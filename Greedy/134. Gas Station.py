'''
https://leetcode.com/problems/gas-station/
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = 0
        r = 0
        n = len(gas)
        rg = 0
       
        while l < n and not (r >= n and r%n == l):
            if rg + gas[r%n] >= cost[r%n]:
                rg = rg + gas[r%n]-cost[r%n]
                r += 1
            else:
                if l < r:
                    rg = rg - gas[l] + cost[l]
                    l += 1         
                else:
                    l += 1
                    r += 1

        if l >= n:
            return -1
        return l


'''
Two Pointer Method (Greedy)

Use Two pointer to track remaingas if we start from first pointer station to the last pointer station.
If adding last station won't allow us to travel to next station remove first stations until we have enough to travel to next station. 
At this point if first and last pointer station are same we need to move both to next station because current station also didn't suffice the condition to travel.

We can end the condition when
1) First pointer station has been check through all the station. this means at any given station traveling in circuit is impossible.
2) If last pointer station as caught up with first pointer station.


RA : O(N)
SA : O(1)



'''