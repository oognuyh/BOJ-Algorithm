"""
    10757. 큰 수 A+B
"""
from sys import stdin

def run(N):
    def getAB():
        A, B = N 
        if len(A) < len(B):
            A, B = B, A
        
        if not (len(A) == len(B)):
            B = '0' * (len(A) - len(B)) + B
        
        return A, B

    A, B = getAB()
    length = len(A)
    added_value = [0 for _ in range(length + 1)]
    

    for i in reversed(range(0, length)):
        added_digits = int(A[i]) + int(B[i]) + added_value[i + 1]
        q, r = divmod(added_digits, 10)

        added_value[i + 1] = r
        added_value[i] += q

    print(int(''.join(map(str, added_value))))

if __name__ == "__main__":
    run(stdin.readline().strip().split())