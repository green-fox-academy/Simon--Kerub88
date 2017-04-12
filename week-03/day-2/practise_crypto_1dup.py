# Create a method that decrypts the texts/duplicated_chars.txt
fr = open("duplicated-chars.txt", "r")
text = fr.read()


def decrypt(text):

    decrypted_text = ""
    for t in range(0, len(text), 2):
        decrypted_text += text[t]
    return decrypted_text

print(decrypt(text))
