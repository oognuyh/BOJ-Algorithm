"""
    11729. 하노이 탑 이동 순서
"""
def hanoi(n, from_bar, by_bar, to_bar):
    if n == 0: return 

    hanoi(n - 1, from_bar, to_bar, by_bar)
    print(f"{from_bar} {to_bar}")
    hanoi(n - 1, by_bar, from_bar, to_bar)

N = int(input()) # 1 <= N <= 20

print(f"{2 ** N - 1}")
hanoi(N, 1, 2, 3)