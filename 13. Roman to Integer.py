'''
經典題型，由於羅馬字母原則上是由大至小排列，故若是發現某一數字大於先前的數字，則代表大 - 小 (e.g., XV = 4)
故作答上只需使用一個迴圈由左掃至右，判斷一下目前的羅罵字與上一個的大小關係，若發現小的字母在大的字母左側，則記得要減去2倍的先前字母值
(不是挺好解釋的，詳情見程式碼)
'''


class Solution:
    def eval_roman(self, symbol):
        answer = 0
        if('I' == symbol):
            answer = 1
        elif('V' == symbol):
            answer = 5
        elif('X' == symbol):
            answer = 10
        elif('L' == symbol):
            answer = 50
        elif ('C' == symbol):
            answer = 100
        elif ('D' == symbol):
            answer = 500
        elif ('M' == symbol):
            answer = 1000

        return answer


    def romanToInt(self, s):
       answer, previous_val, current_val = 0, 0, 0
       for i in s:
           current_val = self.eval_roman(i)
           answer = answer + current_val

           if(current_val > previous_val):
               answer = answer - 2 * previous_val

           previous_val = current_val

       return answer

# 本機端測試用
# sol = Solution()
# print(sol.romanToInt("MCMXCIV"))
# print(sol.romanToInt("XII"))
# print(sol.romanToInt("IV"))
# print(sol.romanToInt("IX"))