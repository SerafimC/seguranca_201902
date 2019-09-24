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

def main():

    key = random_key()
    key_attempt_points = [0 for i in range(255)]
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

    for i, el in enumerate(key_attempt_points, start=0):
        for char in crypted_char_frequencies:
            if char['char'] == i:
                key_attempt_points[i] += char['freq']

    print(key_attempt_points)
    
main()