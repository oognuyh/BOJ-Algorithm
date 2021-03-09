"""
    1934. 최소공배수
"""
from sys import stdin

def run(a, b):
    def gcd(a, b):
        return gcd(b % a, a) if b % a else a

    def lcm(a, b):
        return a * (b // gcd(a, b))
    
    print(lcm(a, b))

if __name__ == "__main__":
    for _ in range(int(stdin.readline().strip())):
        run(*map(int, stdin.readline().strip().split()))
