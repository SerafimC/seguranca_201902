from trie import TS
from char_frequency import message
output_text = ''
output_file = "message.bin"

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[:])

f= open(output_file,"wb")
f.truncate(0) # Limpa o arquivo 

for char in message:
    f.write(bitstring_to_bytes(TS[ord(char)]))

f.close()