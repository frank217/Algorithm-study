#https://leetcode.com/problems/rle-iterator/

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encode = encoding

    def next(self, n: int) -> int:
        while self.encode and n > self.encode[0]:
            n -= self.encode[0]
            self.encode = self.encode[2:] 
        
        if not self.encode:
            return -1

        self.encode[0] -= n
        return self.encode[1]        
        
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)