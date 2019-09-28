from functools import reduce
from char_frequency import char_frequencies, duo_frequencies, trio_frequencies
# https://www.gta.ufrj.br/ensino/eel879/trabalhos_vf_2010_2/gabriel/cript.htm

def random_key():
    return [i for i in reversed(range(255))]

def decrypt_message(crypted_msg, key):
    descrypted_msg = ''
    
    for i in crypted_msg:
        descrypted_msg += chr(key[int(i)])
    return descrypted_msg

def crypt_message(message, key):
    crypted_msg = []
    for i in message:
        crypted_msg.append(key[ord(i)])
    return crypted_msg

def getCharFreqs(crypted_msg):
    crypted_frequencies = [0 for i in range(255)]

    for c in crypted_msg:
        crypted_frequencies[c] += 1

    return [{"char":i, "freq": c / len(crypted_msg)*100} for i, c in enumerate(crypted_frequencies, start=0)]

def getDuoFreqs(crypted_msg):
    duo_dict = {}
    duo_frequencies = [] 
    count = 0

    for i, char in enumerate(crypted_msg, start=0):
        if i >= len(crypted_msg)-1:
            break
        el = str(char)+'|'+str(crypted_msg[i+1])
        if el not in duo_dict:
            duo_dict[el] = 0
        else:
            duo_dict[el] += 1
        count += 1

    for el in duo_dict:
        duo_frequencies.append({"duo":el, "freq": duo_dict[el] / count * 100 })

    return sorted(duo_frequencies, key = lambda i: i['freq'], reverse = True)

def getTrioFreqs(crypted_msg):
    trio_dict = {}
    trio_frequencies = []
    count = 0

    for i, char in enumerate(crypted_msg, start=0):
        if i >= len(crypted_msg)-2:
            break
        el = str(char)+'|'+str(crypted_msg[i+1])+'|'+str(crypted_msg[i+2])
        if el not in trio_dict:
            trio_dict[el] = 0
        else:
            trio_dict[el] += 1
        count += 1

    for el in trio_dict:
        trio_frequencies.append({"trio":el, "freq": trio_dict[el] / count * 100 })

    return sorted(trio_frequencies, key = lambda i: i['freq'], reverse = True)

# def key_permutation(key_attempt, crypted_msg):

def main():

    key = random_key()
    message = [c for c in 'Era uma vez em Hollywood. Filme de Quentin Tarantino. Teste mensagem criptografada. Quanto mais texto, mais facil de identificar os padroes.']
    crypted_msg = crypt_message(message, key)

    crypted_char_frequencies = getCharFreqs(crypted_msg)
    crypted_duo_frequencies = getDuoFreqs(crypted_msg)
    crypted_trio_frequencies = getTrioFreqs(crypted_msg)

    key_attempt = [-1 for i in range(255)]
    sorted_freqs = sorted(char_frequencies, key = lambda i: i['freq'], reverse = True)

    for i, el in enumerate(sorted(crypted_char_frequencies, key = lambda i: i['freq'], reverse = True), start = 0):
        key_attempt[el['char']] = sorted_freqs[i]['char']

    descrypted_msg = decrypt_message(crypted_msg, key_attempt)

    
    
# main()
key = random_key()
message = [c for c in 'Era uma vez em Hollywood. Filme de Quentin Tarantino. Teste mensagem criptografada. Quanto mais texto, mais facil de identificar os padroes.']
crypted_msg = crypt_message(message, key)

key_chars_attempts = [[] for i in range(255)]

key_attempt = [56 for i in range(255)]
sorted_freqs = sorted(char_frequencies, key = lambda i: i['freq'], reverse = True)

crypted_char_frequencies = getCharFreqs(crypted_msg)
crypted_duo_frequencies = getDuoFreqs(crypted_msg)
crypted_trio_frequencies = getTrioFreqs(crypted_msg)

for k, kca in enumerate(key_chars_attempts, start=0):
    for krpt_char in crypted_msg:
        idx = next((index for (index, d) in enumerate(crypted_char_frequencies) if d['char'] == krpt_char), None)
        if idx >= 0:
            for lg_freq in sorted_freqs: 
                key_chars_attempts[k].append({"char": lg_freq['char'] , "prob" : ((lg_freq['freq'] - crypted_char_frequencies[idx]['freq'])**2)**0.5})
                    

for i in range(len(key_chars_attempts)):
    # print(key_chars_attempts[i][:5])
    key_chars_attempts[i] = sorted(key_chars_attempts[i], key = lambda k: k['prob'], reverse = False)

for t in sorted_freqs:
    print(t['char'])

for i, kca in enumerate(key_chars_attempts,start=0):
    if len(kca) > 0:
        key_attempt[i] = kca[0]['char']

descrypted_msg = decrypt_message(crypted_msg, key_attempt)
print(descrypted_msg)

