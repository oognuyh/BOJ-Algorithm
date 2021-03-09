"""
    1019. 책 페이지
    ref : https://nerogarret.tistory.com/36
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(N):
    def add_all():
        for number in range(10):
            counts[number] += (N // 10 + 1) * (10 ** weight)

    def subtract_diff():
        for number in range(10 - diff, 10): # ones
            counts[number] -= (10 ** weight)

        for number in str(N)[:-1]: # others
            counts[int(number)] -= diff * (10 ** weight)

    def subtract_zeros():
        counts[0] -= (10 ** weight)

    def change_ones_to_nine():
        return int(str(N)[:-1] + "9")

    counts = [0 for _ in range(10)]

    for weight in range(len(str(N))):
        changed_N = change_ones_to_nine()
        diff = changed_N - N

        add_all()
        subtract_diff()
        subtract_zeros()

        N //= 10

    print(' '.join(map(str, counts)))

if __name__ == "__main__":
    run(int(read()))