char_frequencies = [0 for i in range(255)]
duo_freq = {}
duo_frequencies = []
tri_freq = {}
lenght=0

with open("texto_base.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if ord(c) < 255:
        lenght += 1
        char_frequencies[ord(c)] += 1

char_frequencies = [{"char":i, "freq": c / lenght*100} for i, c in enumerate(char_frequencies, start=0)]

# print('Alphabetic frequencies:')
# for i in 'abcdefghijklmnopqrstuvwxyz':
#     print(i + ': ' + str(char_frequencies[ord(i)]*100))

# print(sorted(char_frequencies, key = lambda i: i['freq'], reverse = True) )
duo_count = 0
for line in open("texto_base2.txt").readlines():
  for i, char in enumerate(line, start=0):
    if i == len(line)-1:
      break
    if char+line[i+1] not in duo_freq:
      duo_freq[char+line[i+1]] = 0
    else:
      duo_freq[char+line[i+1]] += 1
    duo_count += 1

for el in duo_freq:
  duo_frequencies.append({"duo":el, "freq": duo_freq[el] / duo_count * 100 })

duo_frequencies = sorted(duo_frequencies, key = lambda i: i['freq'], reverse = True)
