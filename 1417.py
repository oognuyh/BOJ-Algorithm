"""
    1417. 국회의원 선거
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(N):
    def get_poll():
        return int(read()), [int(read()) for _ in range(N - 1)]

    def get_greater_than_dasom():
        return [p for p in poll if p > dasom]

    def is_dasom_less_than_others():
        poll.sort()

        return False if not poll else False if poll[-1] < dasom else True

    def bribe():
        nonlocal dasom, answer

        dasom += 1; poll[-1] -= 1; answer += 1

    dasom, poll = get_poll()
    answer = 0

    poll = get_greater_than_dasom()

    while is_dasom_less_than_others():
        bribe()

    print(answer)

if __name__ == "__main__":
    run(int(read()))