# https://www.gta.ufrj.br/ensino/eel879/trabalhos_vf_2010_2/gabriel/cript.htm

crypted_msg = []
descrypted_msg = ''
from char_frequency import char_frequencies, duo_frequencies

def random_char():
    return [i for i in reversed(range(255))]

key = random_char()

# print('Mensagem para cifrar: ')
message = [c for c in 'Era uma vez em Hollywood. Filme de Quentin Tarantino. Teste mensagem criptografada']
# message = [c for c in 'aeiouAEIOU']

for i in message:
    crypted_msg.append(key[ord(i)])

# print('Mensagem descriptografada: ')
# for i in crypted_msg:
#     descrypted_msg += chr(key[int(i)])

# print(descrypted_msg)

crypted_frequencies = [0 for i in range(255)]

for c in crypted_msg:
    crypted_frequencies[c] += 1

crypted_frequencies = [{"char":i, "freq": c / len(crypted_msg)*100} for i, c in enumerate(crypted_frequencies, start=0)]
key_attempt = [-1 for i in range(255)]

sorted_freqs = sorted(char_frequencies, key = lambda i: i['freq'], reverse = True)

for i, el in enumerate(sorted(crypted_frequencies, key = lambda i: i['freq'], reverse = True), start = 0):
    key_attempt[el['char']] = sorted_freqs[i]['char']

print('Mensagem descriptografada: ')
for i in crypted_msg:
    descrypted_msg += chr(key[int(i)])
print(descrypted_msg)
descrypted_msg = ''
for i in crypted_msg:
    # print(key_attempt[int(i)])
    descrypted_msg += chr(key_attempt[int(i)])

print(descrypted_msg)
