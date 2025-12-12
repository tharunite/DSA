1class MinStack:
2
3    def __init__(self):
4        self.stack=[]    
5        self._min=[]
6        
7
8    def push(self, val: int) -> None:
9        self.stack.append(val)
10        if not self._min:
11            self._min.append(val)
12        elif val<self._min[-1]:
13            self._min.append(val) 
14        else :self._min.append(self._min[-1]) 
15        
16
17    def pop(self) -> None:
18        self.stack.pop()
19        self._min.pop()
20
21
22        
23
24    def top(self) -> int:
25        return self.stack[-1]
26        
27
28    def getMin(self) -> int:
29        return self._min[-1]
30        
31
32
33# Your MinStack object will be instantiated and called as such:
34# obj = MinStack()
35# obj.push(val)
36# obj.pop()
37# param_3 = obj.top()
38# param_4 = obj.getMin()