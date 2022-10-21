FibArray = [0, 1]
def Fibonacci(n):
        if n < 0:
            return
        elif n < len(FibArray):
            return FibArray[n]
        else:       
            FibArray.append(Fibonacci(n - 1) + Fibonacci(n - 2))
            return FibArray[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        return Fibonacci(n+1)