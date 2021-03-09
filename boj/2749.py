"""
    2749. 피보나치 수 3
"""
from sys import stdin

MOD = 1000000

def run(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b % MOD, (a + b) % MOD 
    
    print(a)

if __name__ == "__main__":
    N = int(stdin.readline().strip())
    
    # 피보나치 수를 나눈 수는 항상 주기를 갖는다.
    # 피보나치 수를 나누는 수를 k 라고 할 때, k가 10^n이라면 피사노 주기는 15 * 10^(n - 1)
    run(N % (15 * (MOD // 10))) 
    
