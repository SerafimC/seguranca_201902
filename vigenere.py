crypted_msg = ''
descrypted_msg = ''

print('Mensagem para cifrar: ')
message = [c for c in input()]

print('Chave: ')
key = [ord(k) for k in input()]
print(key)

for i in message:
    if ord(i) > 255:
        raise Exception('Invalid input. Character {} does not belong to the alphabet'.format(i))

print('Mensagem criptografada: ')
key_iterator = 0
for i in message:
    crypted_msg += chr((ord(i) + key[key_iterator]) % 255)
    key_iterator = (key_iterator + 1) % len(key)

print(crypted_msg)
key_iterator = 0
print('Mensagem descriptografada: ')
for i in crypted_msg:
    descrypted_msg += chr((ord(i) - key[key_iterator]) % 255)
    key_iterator = (key_iterator + 1) % len(key)

print(descrypted_msg)