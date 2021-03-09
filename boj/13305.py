"""
    13305. 주유소
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(N, distances, prices):
    total, minimum = 0, prices[0]

    for i in range(N - 1):
        minimum = min(minimum, prices[i])
        total += minimum * distances[i]
    
    print(total)

if __name__ == "__main__":
    run(int(read()), list(map(int, read().split())), list(map(int, read().split())))