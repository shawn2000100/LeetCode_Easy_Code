class MinStack(object):
    def __init__(self):
        self.content = list()
        self.size = 0
        
    def push(self, x):
        self.content.append(x)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            return # stack empty!
        self.content.pop()
        self.size -= 1
        
    def top(self):
        if self.size == 0:
            return None
        return self.content[-1]
        
    def getMin(self):
        if self.size == 0:
            return None
        return min(self.content)