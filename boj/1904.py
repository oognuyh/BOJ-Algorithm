"""
    1904. 01 타일
"""
def getCount():
    global counts

    for n in range(2, N): counts.append((counts[n - 2] + counts[n - 1]) % 15746)

    return counts[N - 1]

N = int(input()) # 지원이가 만들 수 있는 길이
counts = [1, 2]

print(counts[N - 1] if N < 3 else getCount())