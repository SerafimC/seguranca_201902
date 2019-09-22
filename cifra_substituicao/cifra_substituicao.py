# https://www.gta.ufrj.br/ensino/eel879/trabalhos_vf_2010_2/gabriel/cript.htm

crypted_msg = []
descrypted_msg = ''
from char_frequency import frequencies

def random_char():

    return [i for i in reversed(range(255))]

key = random_char()

print('Mensagem para cifrar: ')
message = [c for c in input()]

for i in message:
    crypted_msg.append(key[ord(i)])

print(crypted_msg)

print('Mensagem descriptografada: ')
for i in crypted_msg:
    descrypted_msg += chr(key[int(i)])

print(descrypted_msg)
print(frequencies)