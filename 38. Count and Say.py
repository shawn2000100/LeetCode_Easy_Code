class Solution:
    def countAndSay(self, n):
        def ans(n):
            if n == 1:
                return "1"
            else:
                statisc = ""
                consecutive = 1 # 連續計算要從1開始，重要!
                prev_string = ans(n-1) # 呼叫前一條答案字串
                for i in range(1, len(prev_string)):
                    if prev_string[i] == prev_string[i-1]:
                         consecutive += 1
                    else:
                        # 連續斷掉了，就把前面數過的數字以及上一個數字加進字串內
                        statisc += (str(consecutive))
                        statisc += prev_string[i-1]
                        consecutive = 1 # 重置
                # 最後一次判斷
                statisc += (str(consecutive))
                statisc += prev_string[len(prev_string) - 1]

                return statisc
        return ans(n)
            
