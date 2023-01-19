# Medium
# https://leetcode.com/contest/weekly-contest-327/problems/make-number-of-distinct-characters-equal/

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # try to change if char is 
        cnt1,cnt2 = Counter(word1), Counter(word2)
        
        s1,s2 = len(cnt1), len(cnt2)

        if abs(s1-s2) > 2: 
            return False
        
        for c1 in cnt1:
            for c2 in cnt2:
                cnt1[c1] -=1 
                cnt2[c2] -=1
                
                v1 = s1 if cnt1[c1] > 0 else s1-1
                v2 = s2 if cnt2[c2] > 0 else s2-1
                if c1 not in cnt2 or cnt2[c1] == 0:
                    v2 += 1
                if c2 not in cnt1 or cnt1[c2] == 0:
                    v1 += 1
                if v1 == v2:
                    return True
                cnt1[c1] +=1 
                cnt2[c2] +=1
        return False


        

