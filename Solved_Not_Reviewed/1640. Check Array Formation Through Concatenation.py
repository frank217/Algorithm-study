#https://leetcode.com/problems/check-array-formation-through-concatenation/


# 1 : Use reduce to concat list to Str then process
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # a bit over architectured. 
        s = set()
        for piece in pieces:
            v = str(reduce(lambda x,y: str(x) + str(y),piece))
            s.add(v)
        
                        
        prev = ""
        for num in arr:
            prev += str(num)
            if prev in s:
                prev = ""
        
        return prev == ""

# 2 : Better with checking list since int are unique
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # a bit over architectured. 
        s = {}
        for piece in pieces:
            s[piece[0]] = piece
        
        ans = []            
        for num in arr:
            if num in s:
                ans += s[num]
        
        return ans == arr
