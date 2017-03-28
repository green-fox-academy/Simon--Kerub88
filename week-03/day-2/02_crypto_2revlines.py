# Create a method that decrypts texts/reversed_zen_lines.txt
fr = open("reversed-lines.txt")
text = fr.readlines()

def decrypt(file_name):
    decode_text = ""
    for t in range(0, len(file_name)):
        decode_text += file_name[-t]
    return decode_text

print(decrypt(text))
