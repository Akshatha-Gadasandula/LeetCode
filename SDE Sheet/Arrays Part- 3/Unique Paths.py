class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        output = 1
        for i in range(m-1):
            output = output*(n+i)//(i+1)
        return (output)
