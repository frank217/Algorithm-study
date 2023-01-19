# hard 
# https://leetcode.com/contest/weekly-contest-327/problems/time-to-cross-a-bridge/
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # Lowest efficiency
        # Rule 1 : only 1 can be crossing bridge.  
        # Rule 2 : right crosses first
        # Rule 3 : lowest efficiency crosses first
        
        # Get lowest time. 
        ctime = 0
        efficiency = [ t[0] + t[2] for t in time]
        l,r,lw,rw = [ (-efficiency[i],-i)for i in range(k)],[],[],[]
        heapq.heapify(l)
        while n > 0 or r or rw:
            #print(ctime,n,l,r,lw,rw)
            while rw and  rw[0][0] <= ctime:
                i = heapq.heappop(rw)[1]
                heapq.heappush(r,(-efficiency[i],-i))
            while lw and lw[0][0] <= ctime:
                i = heapq.heappop(lw)[1]
                if n > 0 : 
                    heapq.heappush(l,(-efficiency[i],-i))
            if r:
                worker = -heapq.heappop(r)[1]
                ctime += time[worker][2]
                heapq.heappush(lw,(ctime+time[worker][3],worker))
                #print("r crossing",ctime,worker)

            elif l:
                worker = -heapq.heappop(l)[1]
                if n > 0:
                    ctime += time[worker][0]
                    heapq.heappush(rw,(ctime+time[worker][1],worker))
                    n -= 1
                    #print("l crossing",ctime,worker,n)

            else:
                if rw and lw:
                    ctime = min(rw[0][0],lw[0][0])
                elif rw:
                    ctime = rw[0][0]
                else:
                    ctime = lw[0][0]
        return ctime