# Create a method that decrypts texts/reversed_zen_order.txt
fr = open("reversed-order.txt")
text = fr.readlines()

def decrypt(text_content):
    text_content = text_content[::-1]
    decode_text = ""
    for line in text_content:
        decode_text += line
    return decode_text

print(decrypt(text))
