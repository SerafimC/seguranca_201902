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

for c in char_frequencies:
    if c['freq'] > 0:
        # print('char: ' + chr(c['char']) + '['+ str(c['char']) + '] ' + str(c['freq']))
        tree_nodes.append(Node(c['char'], c['freq']))



while len(tree_nodes) > 1 :
    x = tree_nodes[0]
    y = tree_nodes[1]
    parent = Node('', x.freq + y.freq, x, y)
    tree_nodes.pop(0)
    tree_nodes.pop(0)
    tree_nodes.append(parent)
    tree_nodes = sorted(tree_nodes, key = lambda k: k.freq)
    
    
def printNode(node, prefix):
    if node:
        printNode(node.left, prefix + '-')
        print(prefix + str(node.char))
        printNode(node.right, prefix + '-')
        
    return
TS = {}
def getTS(node, prefix):
    if node:
        getTS(node.left, prefix+'0')
        if node.char != '':
            TS[node.char] =  prefix
        getTS(node.right, prefix+'1')

getTS(tree_nodes[0], '')

print(TS)
# printNode(tree_nodes[0], '')
