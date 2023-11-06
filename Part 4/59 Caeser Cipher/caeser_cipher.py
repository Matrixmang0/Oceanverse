# Define the lowercase and uppercase alphabets
alpha = 'abcdefghijklmnopqrstuvwxyz'
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define special characters
spl_chr = '[@_!#$%^&*,.()<>?/\|}{~:;+-] '

def caeser_encrypt(string, key):
    """
    Encrypt a string using the Caesar cipher with a given key.

    Args:
        string (str): The input string to be encrypted.
        key (int): The encryption key.

    Returns:
        str: The encrypted string.
    """
    new_str = ""

    # Iterate through each character in the input string
    for i in range(len(string)):
        # Check if the character is not a special character
        if string[i] not in spl_chr:
            # Check if the character is uppercase
            if string[i].isupper():
                ind = Alpha.index(string[i])
                newind = (ind + key) % 26  # Apply the Caesar cipher shift
                new_str += Alpha[newind]
            else:
                ind = alpha.index(string[i])
                newind = (ind + key) % 26  # Apply the Caesar cipher shift
                new_str += alpha[newind]
        else:
            # Keep special characters unchanged
            new_str += string[i]

    return new_str

def caeser_decrypt(string, key):
    """
    Decrypt a string encrypted using the Caesar cipher with a given key.

    Args:
        string (str): The encrypted string to be decrypted.
        key (int): The decryption key.

    Returns:
        str: The decrypted string.
    """
    new_str = ""

    # Iterate through each character in the input string
    for i in range(len(string)):
        # Check if the character is not a special character
        if string[i] not in spl_chr:
            # Check if the character is uppercase
            if string[i].isupper():
                ind = Alpha.index(string[i])
                newind = (ind - key) % 26  # Apply the Caesar cipher reverse shift
                new_str += Alpha[newind]
            else:
                ind = alpha.index(string[i])
                newind = (ind - key) % 26  # Apply the Caesar cipher reverse shift
                new_str += alpha[newind]
        else:
            # Keep special characters unchanged
            new_str += string[i]

    return new_str

# Example sentence to be encrypted and decrypted
sentence = "Hello, how are you?"

# Encrypt the sentence with a key of 4
encrypted = caeser_encrypt(sentence, 4)
print("Encrypted:", encrypted)

# Decrypt the encrypted sentence with the same key of 4
decrypted = caeser_decrypt(encrypted, 4)
print("Decrypted:", decrypted)