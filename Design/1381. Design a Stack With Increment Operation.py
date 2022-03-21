'''
https://leetcode.com/problems/design-a-stack-with-increment-operation/

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
'''


class CustomStack:
    
    def __init__(self, maxSize: int):
        self.stack = [None for i in range(maxSize)]
        self.s = 0
    def push(self, x: int) -> None:
        if self.s < len(self.stack):
            self.stack[self.s] = x
            self.s += 1

    def pop(self) -> int:
        if self.s > 0:
            val = self.stack[self.s-1]
            self.s -= 1
        else:
            val = -1
        return val

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.s)):
            self.stack[i] = self.stack[i] + val
            




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)