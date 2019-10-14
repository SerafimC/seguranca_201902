from char_frequency import char_frequencies
tree_nodes = []

class Node:
    def __init__(self, char, freq, left=None, right=None) :
        self.char = char
        self.freq = freq
        self.left  = left
        self.right = right

    def __str__(self) :
        return str(self.freq)

class Tree:
    def __init__(self, node):
        self.root = node

    def insert(self, node):
        current = self.root
        cursor = self.root
        while(not cursor):
            current = cursor
            if node.freq >= cursor.freq:
                pass
            else:
                pass

for c in char_frequencies:
    if c['freq'] > 0:
       tree_nodes.append(Node(c['char'], c['freq']))

tree = None
x = tree_nodes[0]
y = tree_nodes[1]
parent = Node('', x.freq + y.freq, x, y)
tree_nodes.pop(0)
tree_nodes.pop(0)
if not tree:
    tree = Tree(parent)
else:
    tree.insert(parent)