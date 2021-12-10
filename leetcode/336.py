"""
    336. Palindrome Pairs
"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = { word: index for index, word in enumerate(words) }
        pairs = set()
        
        for i, word in enumerate(words):
            if (reversed_word := word[::-1]) in d and d[reversed_word] != i:
                pairs.add((d[reversed_word], i))
                
            for j in range(1, len(word)):
                prefix, suffix = word[:j], word[j:]
                
                if prefix == prefix[::-1] and suffix[::-1] in d:
                    pairs.add((d[suffix[::-1]], i))
                if suffix == suffix[::-1] and prefix[::-1] in d:
                    pairs.add((i, d[prefix[::-1]]))
                    
            if word and word == reversed_word and "" in d:
                pairs |= set(((i, d[""]), (d[""], i)))
                
        return pairs

"""
    - 2460 ms 27.9 MB
"""