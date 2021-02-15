"""
    1251. 단어 나누기
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(word):
    def flip(part):
        return part[::-1]

    def get_new_word():
        return flip(word[:left]) + flip(word[left:right]) + flip(word[right:])
    
    minimum = "z" * len(word)

    for left in range(1, len(word) - 1):
        for right in range(left + 1, len(word)):
            new_word = get_new_word()
            minimum = minimum if minimum < new_word else new_word

    print(minimum)

if __name__ == "__main__":
    run(read())