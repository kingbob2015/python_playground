from collections import deque

class TrieNode():
    def __init__(self):
        #only fill out data if it is end of a valid sequence
        self.data = None
        #going dict here to support wider range of variable characters with lower memory
        self.children = {}
    
    def __str__(self):
        return(f"Data Contained: {self.data} - Children At: {' '.join(self.children.keys())}")

class Trie():
    def __init__(self):
        self.root = TrieNode()
            
    def insert(self, value):
        currentNode = self.root
        try:
            for char in value:
                if char not in currentNode.children:
                    currentNode.children[char] = TrieNode()
                currentNode = currentNode.children[char]
            currentNode.data = value
        except Exception as e:
            print(e)
            return False
        return True

    def contains(self, target, substring=False):
        currentNode = self.root
        for char in target:
            if char not in currentNode.children:
                return False
            else:
                currentNode = currentNode.children[char]
        if substring:
            return True
        elif currentNode.data == target:
            return True
        else:
            return False
    


if __name__ == '__main__':
    t = Trie()
    t.insert("Testinga")
    print(t.contains("Testing", True))



    