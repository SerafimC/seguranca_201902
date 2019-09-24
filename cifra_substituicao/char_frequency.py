filename = "texto_base2.txt"

def get_frequencies(filename):
  char_frequencies = [0 for i in range(255)]
  duo_freq = tri_freq =  {}
  duo_frequencies = trio_frequencies = []
  lenght=0

  with open(filename) as f:
    while True:
      c = f.read(1)
      if not c:
        break
      if ord(c) < 255:
          lenght += 1
          char_frequencies[ord(c)] += 1

  char_frequencies = [{"char":i, "freq": c / lenght*100} for i, c in enumerate(char_frequencies, start=0)]

  count = 0
  for line in open(filename).readlines():
    for i, char in enumerate(line, start=0):
      if i == len(line)-1:
        break
      if char+line[i+1] not in duo_freq:
        duo_freq[char+line[i+1]] = 0
      else:
        duo_freq[char+line[i+1]] += 1
      count += 1

  for el in duo_freq:
    duo_frequencies.append({"duo":el, "freq": duo_freq[el] / count * 100 })

  duo_frequencies = sorted(duo_frequencies, key = lambda i: i['freq'], reverse = True)

  count = 0
  for line in open(filename).readlines():
    for i, char in enumerate(line, start=0):
      if i >= len(line)-2:
        break
      if char+line[i+1]+line[i+2] not in tri_freq:
        tri_freq[char+line[i+1]+line[i+2]] = 0
      else:
        tri_freq[char+line[i+1]+line[i+2]] += 1
      count += 1

  for el in tri_freq:
    trio_frequencies.append({"trio":el, "freq": tri_freq[el] / count * 100 })

  trio_frequencies = sorted(trio_frequencies, key = lambda i: i['freq'], reverse = True)

  return char_frequencies, duo_frequencies, trio_frequencies

char_frequencies, duo_frequencies, trio_frequencies = get_frequencies(filename)