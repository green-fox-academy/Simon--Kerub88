# Create a method that decrypts texts/reversed_zen_lines.txt
fr = open("reversed-lines.txt", "r")
text = fr.readlines()

def decrypt(text):
    decrypted_text = ""
    for lines in text:
        decrypted_text += lines[::-1]
    return decrypted_text

print(decrypt(text))
