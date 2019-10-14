from huffman import HuffmanCoding
filename = "message.txt"

h = HuffmanCoding(filename)

output_path = h.compress()
h.decompress(output_path)