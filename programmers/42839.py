"""
    42839. 소수 찾기
"""
from itertools import permutations
from math import sqrt

def solution(numbers):
    def is_prime(number):
        if number < 2: return False

        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0: return False

        return True

    primes = []

    for i in range(len(numbers)):
        for number in set(map(lambda possible: int(''.join(possible)), permutations(numbers, i + 1))):
            if is_prime(number):
                primes.append(number)
            
    return len(set(primes))

"""
    # Others
        1. Sieve of Eratosthenes
            from itertools import permutations
            
            def solution(n):
                a = set()
                for i in range(len(n)):
                    a |= set(map(int, map("".join, permutations(list(n), i + 1))))
                a -= set(range(0, 2))
                for i in range(2, int(max(a) ** 0.5) + 1):
                    a -= set(range(i * 2, max(a) + 1, i))
                return len(a)

        2. Recursion
            primeSet = set()

            def isPrime(number):
                if number in (0, 1):
                    return False
                for i in range(2, number):
                    if number % i == 0:
                        return False

                return True


            def makeCombinations(str1, str2):
                if str1 != "":
                    if isPrime(int(str1)):
                        primeSet.add(int(str1))

                for i in range(len(str2)):
                    makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


            def solution(numbers):
                makeCombinations("", numbers)

                answer = len(primeSet)

                return answer
"""