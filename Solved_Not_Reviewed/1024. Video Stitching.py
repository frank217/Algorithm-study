#https://leetcode.com/problems/video-stitching/description/

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # This is greedy scheduling.
        # Sort the Clips with start time 
        clips.sort()
        # remove all the start time greater then time
        while clips[-1][0] > time:
            clips.pop()
        
        # Reverse Clips to iterate from largest start to smallest start
        clips.reverse()

        ans = [] 
        for start,end in clips:
            if ans and ans[-1][0]== start:
                continue 
            while ans:
                prev = ans.pop()
                if (ans and ans[-1][0] <= end) or end >= time:
                    continue
                else:
                    ans.append(prev)
                    break
            ans.append([start,end])

        # Endtime not match
        if ans[0][1] < time :
            return -1
        # starttime not match. 
        if ans[-1][0] != 0:
            return -1
        
        # Check that there is overlap
        for i in range(1,len(ans)):
            if  ans[i-1][0] > ans[i][1] :
                return -1
        return len(ans)
