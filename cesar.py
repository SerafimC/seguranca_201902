crypted_msg = ''
descrypted_msg = ''

print('Mensagem para cifrar: ')
message = [c for c in input()]

print('Chave: ')
key = ord(input()[0])

for i in message:
    if ord(i) > 255:
        raise Exception('Invalid input. Character {} does not belong to the alphabet'.format(i))

print('Mensagem criptografada: ')
for i in message:
    crypted_msg += chr((ord(i) + key) % 255)

print(crypted_msg)

print('Mensagem descriptografada: ')
for i in crypted_msg:
    descrypted_msg += chr((ord(i) - key) % 255)

print(descrypted_msg)