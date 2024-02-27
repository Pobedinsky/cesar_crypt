def encode(text, k):
  return ''.join(chr((ord(x) + k % 26)%26 + 65) if x != ' ' else ' ' for x in text.upper())

def decode(text, k):
  return encode(text, -k)
