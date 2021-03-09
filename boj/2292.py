"""
    2292. 벌집
"""
get = lambda x : (3 + (9 - (12 * (2 - x))) ** (1/2)) / 6 if not x == 1 else 0
print(int(get(int(input()))) + 1)