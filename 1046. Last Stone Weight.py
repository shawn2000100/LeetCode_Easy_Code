class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) >= 2:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if y == x:
                continue
            elif y > x:
                stones.append(y - x)
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]