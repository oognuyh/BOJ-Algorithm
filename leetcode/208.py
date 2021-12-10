"""
    208. Implement Trie (Prefix Tree)
"""
class Node:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root

        for character in word:
            current_node = current_node.children[character]

        current_node.is_word = True
        
    def search(self, word: str) -> bool:
        current_node = self.root

        for character in word:
            if character not in current_node.children: return False
            current_node = current_node.children[character]

        return current_node.is_word

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        for character in prefix:
            if character not in current_node.children: return False
            current_node = current_node.children[character]

        return True

"""
    - 255 ms 33.2 MB
"""