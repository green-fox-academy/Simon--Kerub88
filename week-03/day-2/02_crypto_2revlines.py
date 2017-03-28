# Create a method that decrypts texts/reversed_zen_lines.txt
fr = open("reversed-lines.txt")
text = fr.readlines()

def decrypt(text_content):
    decode_text = ""
    for line in range(0, len(text)):
        decode_text += text[line][::-1]
    return decode_text

print(decrypt(text))
