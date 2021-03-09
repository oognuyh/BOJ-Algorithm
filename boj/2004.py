"""
    2004. 조합 0의 개수
"""
def count(number, target):
    total, i = 0, number

    while i <= target:
        total += target // i
        i *= number       

    return total

n, m = map(int, input().split())
five = count(5, n) - count(5, n - m) - count(5, m)
two = count(2, n) - count(2, n - m) - count(2, m)
print(five if five < two else two)