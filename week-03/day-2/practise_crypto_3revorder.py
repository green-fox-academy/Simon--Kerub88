# Create a method that decrypts texts/reversed_zen_order.txt
fr = open("reversed-order.txt", "r")
text = fr.readlines()

def decrypt(text):
    decrypted_text = ""
    text = text[::-1]
    for line in text:
        decrypted_text += line
    return decrypted_text

print(decrypt(text))
