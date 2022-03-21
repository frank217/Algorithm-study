'''
https://leetcode.com/problems/design-an-ordered-stream/
'''
class OrderedStream:

    def __init__(self, n: int):
        self.p = 0
        self.a = [-1 for i in range(n)]

    def insert(self, idKey: int, value: str) -> List[str]:
        index = idKey-1
        self.a[index] = value
        
        result = []
        if index == self.p:
            while index < len(self.a):
                if self.a[index] == -1:
                    break
                index+=1
            result =  self.a[self.p:index]
            self.p = index
        return result
    
