"""
    12015. 가장 긴 증가하는 부분 수열 2
"""
from sys import stdin
from bisect import bisect_left
read = stdin.readline

def run(N):
    def getA():
        return list(map(int, read().strip().split()))

    increasingArr = []
    A = getA()

    for a in A:
        index = bisect_left(increasingArr, a)
        if len(increasingArr) == index:
            increasingArr += [a]
        else:
            increasingArr[index] = a

    print(len(increasingArr))

if __name__ == "__main__":
    run(int(read().strip()))