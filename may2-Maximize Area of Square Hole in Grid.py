class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        max_v_run = 1
        max_h_run = 1
        vBars.sort()
        hBars.sort()
        curr_run = 1

        for i in range(1, len(vBars)):
            if vBars[i - 1] == vBars[i] - 1:
                curr_run += 1
            else:
                max_v_run = max(max_v_run, curr_run)
                curr_run = 1

        max_v_run = max(max_v_run, curr_run)

        curr_run = 1
        for i in range(1, len(hBars)):
            if hBars[i - 1] == hBars[i] - 1:
                curr_run += 1
            else:
                max_h_run = max(max_h_run, curr_run)
                curr_run = 1
        max_h_run = max(max_h_run, curr_run)
    

        
        remove = min(max_v_run, max_h_run)
        return (remove + 1) ** 2
        
        
