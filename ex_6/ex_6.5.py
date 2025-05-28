str = 'X-DSPAM-Confidence:    0.8475'
colon = str.find(':')
# print(colon)
piece = str[colon+1:]
# print(piece)
value = float(piece)
print(value)