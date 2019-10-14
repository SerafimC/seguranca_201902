filename = "message.txt"

def get_frequencies(filename):
  char_frequencies = [0 for i in range(255)]
  lenght=0

  with open(filename) as f:
    while True:
      c = f.read(1)
      if not c:
        break
      if ord(c) < 255:
          lenght += 1
          char_frequencies[ord(c)] += 1
  
  return sorted([{"char":i, "freq": c / lenght*100} for i, c in enumerate(char_frequencies, start=0)], key = lambda i: i['freq'], reverse = False)

char_frequencies = get_frequencies(filename)