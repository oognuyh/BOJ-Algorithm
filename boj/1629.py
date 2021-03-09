"""
    1629. 곱셈
"""
from sys import stdin

def divide(A, B, C):
    if B == 1:
        return A % C 

    return divide(A, B - 1, C) * A % C if B % 2 == 1 else (divide(A, B // 2, C) ** 2) % C

if __name__ == "__main__":
    A, B, C = map(int, stdin.readline().strip().split())
    print(divide(A, B, C)) # A, B, C는 모두 2,147,483,647 이하의 자연수
    # print(pow(A, B, C)) 내장 함수를 이용하면 쉽게 구할 수 있음. 세 번째 인자를 추가하면 C로 나눈 나머지 값을 출력