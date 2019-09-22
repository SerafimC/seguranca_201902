frequencies = [0 for i in range(255)]
lenght=0

with open("texto_base.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if ord(c) < 255:
        lenght += 1
        frequencies[ord(c)] += 1

frequencies = [i / lenght*100 for i in frequencies]

# print('Alphabetic frequencies:')
# for i in 'abcdefghijklmnopqrstuvwxyz':
#     print(i + ': ' + str(frequencies[ord(i)]*100))