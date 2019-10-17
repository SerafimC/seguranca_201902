from trie import TS
file = "message.bin"
message = ''

with open(file, mode='rb') as f:
    c = f.read()
    print(c.decode('utf8'))

