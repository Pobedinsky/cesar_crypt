def encode(text, k):
  return ''.join(chr(ord(x) + k % 26) if x != ' ' else ' ' for x in text)

def decode(text, k):
  return encode(text, -k)
