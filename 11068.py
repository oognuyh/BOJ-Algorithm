"""
    11068. 회문인 수
"""
from sys import stdin

def run():
    def convert(n, base):
        converted = []
        while n > 0:
            converted.insert(0, n % base)
            n //= base
        
        return converted

    def is_palidrome(number): 
        return True if number == number[::-1] else False

    for number in numbers:
        is_possible = False

        for base in range(2, 65):
            converted_number = convert(number, base)

            if is_palidrome(converted_number):
                is_possible = True; break

        print(1 if is_possible else 0)

if __name__ == "__main__":
    T = int(stdin.readline().strip())
    numbers = [int(stdin.readline().strip()) for _ in range(T)]

    run()
