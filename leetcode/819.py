"""
    819. Most Common Word
"""
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[^a-z]", ' ', paragraph.lower())        
        
        counter = Counter([word for word in paragraph.split() if word not in banned])
        
        return counter.most_common(1)[0][0]
"""
    - 40 ms 14.5 MB

    # Others 
        1. re.split + max with key - 24 ms 14.2 MB
            a = re.split(r'\W+', paragraph.lower())
            b = [w for w in a if w not in banned]
            return max(b, key = b.count)

        2. dict - 24 ms 14.1 MB
            dict = {}
            banned = set(banned)
            for c in "!?',;.":
                paragraph = paragraph.replace(c, " ")
            paragraph = paragraph.lower().split()

            for word in paragraph:            
                if word not in banned:
                    if word in dict:
                        dict[word]+=1
                    else:
                        dict[word]=1

            return max(dict, key=dict.get)

    # Tips
        1. "\W" means [^A-z0-9__]
        2. max() can be used with key like len or count ..
"""