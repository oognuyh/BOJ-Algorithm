"""
    6549. 히스토그램에서 가장 큰 직사각형
    ref : https://kunkunwoo.tistory.com/71
"""
from sys import stdin

def run(heights):
    def solve(left, right):
        if left == right: return heights[left]

        mid = (left + right) // 2
        ret = max(solve(left, mid), solve(mid + 1, right))
        lo, hi = mid, mid + 1
        height = min(heights[lo], heights[hi])
        ret = max(ret, height * 2)

        while left < lo or hi < right:
            if hi < right and (lo <= left or heights[lo - 1] < heights[hi + 1]):
                hi += 1
                height = min(height, heights[hi])
            else:
                lo -= 1
                height = min(height, heights[lo])
            
            ret = max(ret, height * (hi - lo + 1))

        return ret 

    length, heights = heights[0], heights[1:]

    return solve(0, length - 1)

if __name__ == "__main__":
    while True:
        heights = stdin.readline().strip()
        if heights[0] == '0':
            break

        heights = list(map(int, heights.split()))

        print(run(heights))        