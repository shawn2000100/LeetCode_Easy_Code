class Solution:
    def judgeCircle(self, moves):
        # �k�@
        # x_dist, y_dist = 0, 0
        # for cmd in moves:
        #     if cmd == 'U':
        #         y_dist += 1
        #     elif cmd == 'D':
        #         y_dist -= 1
        #     elif cmd == 'L':
        #         x_dist -= 1
        #     elif cmd == 'R':
        #         x_dist += 1
        # return x_dist == y_dist == 0
        
        # �k�G
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')