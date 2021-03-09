"""
    10816. 숫자 카드 2
"""
from sys import stdin
import bisect
def read():
    return stdin.readline().strip()

def run(N_COUNT, N, M_COUNT, M):
    def get_idx_to_be_inserted():
        return bisect.bisect_left(N, M[idx_m]) 

    def is_in_N():
        return idx < N_COUNT and N[idx] == M[idx_m]

    def get_last_idx():
        return bisect.bisect_left(N, M[idx_m] + 1)

    for idx_m in range(M_COUNT):
        idx = get_idx_to_be_inserted()
        
        print(get_last_idx() - idx if is_in_N() else 0, end = " ")

if __name__ == "__main__":
    run(
        int(read()),
        list(sorted(map(int, read().split()))),
        int(read()),
        list(map(int, read().split()))
    ) 