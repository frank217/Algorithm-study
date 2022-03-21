'''
https://leetcode.com/problems/cinema-seat-allocation/
'''

from collections import defaultdict
from tokenize import group


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        seatHash = defaultdict(set)
        for r,c in reservedSeats:
            if c >= 2 and  c <= 5 :
                seatHash[r].add(1)
            if c >= 4 and c <=7 :
                seatHash[r].add(2) 
            if c >= 6 and c <=9 :
                seatHash[r].add(3) 
                
        groupAllocated = 2*(n-len(seatHash))
        print(groupAllocated)
        for r,notPossibleSeat in seatHash.items():
            print(r,notPossibleSeat)
            if len(notPossibleSeat) != 3:
                groupAllocated += 1
        return groupAllocated


'''
solution(Cache Greed)

Cache possible group of seat that are not possible. for each row.
So if the the seat group is not in the cache it is possible to allocate. 
Row not in cache mean we can have maximum of 2
For each if we have at least one value in the cache for each row maxium seat we can allocate is 1.
    Case when 3 in cache for that row all seat allocation is not possible. 
    Case when 2 in the cache at least one seat is possible. 
    Case when 1 in the cache 
        If it is group1, only group3 can be allocated
        If it is group2, this case is not possible because any value in group will intercet with group1 or group3.
        If it is group3, only group1 can be allocated. 

So if len of cache in the row is not 3 then we can safely assign 1 more group seat. 

RA : O(n)
SA : O(n)

'''