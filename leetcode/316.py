"""
    316. Remove Duplicate Letters
"""
import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, deque = collections.Counter(s), collections.deque()

        for character in s:
            counter[character] -= 1
            if character in deque: continue

            while deque and character < deque[-1] and counter[deque[-1]] > 0:
                deque.pop()

            deque.append(character)

        return deque
        
"""
    - 40 ms	14.1 MB

    # Others
        1. recursion - 52 ms 14.2 MB
            for character in sorted(set(s)):
                suffix = s[s.index(character):]
                if set(s) == set(suffix):
                    return character + self.removeDuplicateLetters(suffix.replace(character, ""))
            return ""

        2. dict, enumerate - 36 ms 14.3 MB
            deque, dictionary = collections.deque(), {character : index for index, character in enumerate(s)}

            for index, character in enumerate(s):
                if character in deque: continue

                while deque and index < dictionary[deque[-1]] and character < deque[-1]:
                    deque.pop()
                deque.append(character)

            return ''.join(deque)
"""