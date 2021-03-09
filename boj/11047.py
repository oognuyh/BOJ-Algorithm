"""
    11047. 동전 0
"""
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins = [coin for coin in coins if coin <= K]

count = 0

for coin in coins[::-1]:
    if K // coin > 0:
        count += K // coin
        K %= coin

print(count)