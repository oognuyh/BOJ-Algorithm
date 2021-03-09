"""
    11401. 이항 계수 3
"""
from sys import stdin

p = 1000000007

def divide(a, b):
    if b == 1: return a % p 
    elif b == 2: return (a ** 2) % p 
    
    return (divide(a, b // 2) ** 2) % p if b % 2 == 0 else a * ((divide(a, b // 2) ** 2) % p)
    
if __name__ == "__main__":
    N, K = map(int, stdin.readline().strip().split()) # 자연수 N과 정수 K

    factorial = [1 for _ in range(N + 1)]
    
    for i in range(2, N + 1):
        factorial[i] = factorial[i - 1] * i % p
    
    # N! % p * (K!*(N - K)!)^(p - 2) % p (페르마의 소정리)
    print((factorial[N] * divide((factorial[N - K] * factorial[K]) % p, p - 2)) % p)
