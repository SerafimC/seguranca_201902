crypted_msg = []
line = []
descrypted_msg = []

print('Mensagem para cifrar: ')
message = [c for c in input()]

key = int(len(message) / 2)

key_iterator = 0
for c in message:
    if key_iterator == key:
        crypted_msg.append(line)
        line = []
        key_iterator = 0
    line.append(c)
    key_iterator += 1
crypted_msg.append(line)

crypted_msg = [[crypted_msg[j][i] for j in range(len(crypted_msg))] for i in range(len(crypted_msg[0]))] 
msg = ''
for line in crypted_msg:
    for col in line:
        msg += col

print()
print("Crypted message: ")
print(msg)

descrypted_msg = [[crypted_msg[j][i] for j in range(len(crypted_msg))] for i in range(len(crypted_msg[0]))] 
msg= ''
for line in descrypted_msg:
    for col in line:
        msg += col

print()
print("Descrypted message: ")
print(msg)
