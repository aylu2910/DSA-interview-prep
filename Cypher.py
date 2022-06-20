import string

alphabet = list(string.ascii_lowercase)


def cipher(string, key):
    string_cipher = ""
    for s in string:
        s_index = alphabet.index(s)
        key_cipher = (key + s_index) % len(alphabet)
        string_cipher += alphabet[key_cipher]

    return string_cipher
