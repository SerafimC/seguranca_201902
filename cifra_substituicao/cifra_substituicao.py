from functools import reduce
from char_frequency import char_frequencies, duo_frequencies, trio_frequencies, message_file, dictionary
# https://www.gta.ufrj.br/ensino/eel879/trabalhos_vf_2010_2/gabriel/cript.htm

def random_key():
    return [i for i in reversed(range(255))]

def decrypt_message(crypted_msg, key):
    descrypted_msg = ''
    
    for i in crypted_msg:
        descrypted_msg += chr(key[i])
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

key = random_key()
message = [c for c in message_file]
crypted_msg = crypt_message(message, key)

key_attempt = [-1 for i in range(255)]
key_chars_attempts = [[] for i in range(255)]
sorted_freqs = sorted(char_frequencies, key = lambda i: i['freq'], reverse = True)

crypted_char_frequencies = getCharFreqs(crypted_msg)
crypted_duo_frequencies = getDuoFreqs(crypted_msg)
crypted_trio_frequencies = getTrioFreqs(crypted_msg)

for k, kca in enumerate(key_chars_attempts, start=0):

    idx_lg = next((index for (index, d) in enumerate(sorted_freqs) if d['char'] == k), -1)
    
    for l, krp_char in enumerate(crypted_char_frequencies, start=0):        
        idx_kca = next((index for (index, d) in enumerate(key_chars_attempts[k]) if d['char'] == k), -1)
           
        if sorted_freqs[idx_lg]['freq'] == 0 and krp_char['freq'] == 0:
            key_chars_attempts[krp_char['char']].append({"char": k, "prob" : 0.0 })
        else:
            key_chars_attempts[krp_char['char']].append({"char": k , "prob" : (100 -((sorted_freqs[idx_lg]['freq'] - krp_char['freq'])**2)**0.5) })

for i in range(len(key_chars_attempts)):
    key_chars_attempts[i] = sorted(key_chars_attempts[i], key = lambda k: k['prob'], reverse = True)

for i, kca in enumerate(key_chars_attempts,start=0):
    key_attempt[i] = kca[0]['char'] 

points = 0
prev_points = 0

kpt_alph = set(crypted_msg)
iterator = 0
iterator_kpt = 0

while(points < 14):
    points = 0 
    key_attempt_copy = key_attempt.copy()

    for i, kca in enumerate(key_chars_attempts,start=0):
        if i == iterator_kpt:
            key_attempt[i] = kca[iterator]['char'] 
    
    descrypted_msg = decrypt_message(crypted_msg, key_attempt)

    for dict in dictionary:
        for word in descrypted_msg.split(' '):
            if dict == word:
                # print(word)
                points += 1
    print(points)
    if points < prev_points:
        key_attempt = key_attempt_copy.copy()

    iterator = (iterator + 1) % len(key_attempt)
    iterator_kpt = (iterator_kpt + 1) % len(kpt_alph)
    prev_points = points

descrypted_msg = decrypt_message(crypted_msg, key_attempt)
print(descrypted_msg)