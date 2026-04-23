class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def get_n(num):
            #x^2 + x - 2c = 0
            x1 = (-1 + sqrt(1 + 8*num))/2
            x2 = (-1 - sqrt(1 + 8*num))/2

            return min(x1, x2) if x1 >= 0 and x2 >= 0 else max(x1, x2)


        def get_result(num):
            lst = [get_n(num/workerTimes[i]) for i in range(len(workerTimes))]
            flag = False
            for i in lst:
                if int(i) == i:
                    flag = True
                    break
            
            return [flag, sum([int(i) for i in lst])]

        ans = [max(workerTimes)*(mountainHeight*(mountainHeight+1)//2)]
        def get_ans(left, right):
            if left > right:
                return

            mid = (left+right)//2
            lst = get_result(mid)
            if lst[1] >= mountainHeight:
                if lst[0]:
                    ans[0] = min(mid, ans[0])
                get_ans(left, mid - 1)
            else:
                get_ans(mid + 1, right)

        
        get_ans(0, max(workerTimes)*(mountainHeight*(mountainHeight+1)//2))
        return ans[0]
            
