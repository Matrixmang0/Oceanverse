alpha = 'abcdefghijklmnopqrstuvwxyz'
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

spl_chr = '[@_!#$%^&*,.()<>?/\|}{~:;+-] '

def caeser_encrypt(string, key):

  new_str = ""

  for i in range(len(string)) :
    if string[i] not in spl_chr:
      if string[i].isupper():
        ind = Alpha.index(string[i])
        newind = (ind + key)%26
        new_str += Alpha[newind]
      else:
        ind = alpha.index(string[i])
        newind = (ind + key)%26
        new_str += alpha[newind]
    else:
      new_str += string[i]

  return new_str

def caeser_decrypt(string, key):

  new_str = ""

  for i in range(len(string)) :
    if string[i] not in spl_chr:
      if string[i].isupper():
        ind = Alpha.index(string[i])
        newind = (ind - key)%26
        new_str += Alpha[newind]
      else:
        ind = alpha.index(string[i])
        newind = (ind - key)%26
        new_str += alpha[newind]
    else:
      new_str += string[i]

  return new_str


sentence = "Hello, how are you?"

encrypted = caeser_encrypt(sentence, 4)
print(encrypted)

decrypted = caeser_decrypt(encrypted, 4)
print(decrypted)

