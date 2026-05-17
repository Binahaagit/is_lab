text = input("Enter text: ").upper()
key = 3

enc = ""
for ch in text:
   enc += chr((ord(ch) - 65 + key) % 26 + 65)
print("Encrypted:", enc)

dec = ""
for ch in enc:
   dec += chr((ord(ch) - 65 - key) % 26 + 65)
print("Decrypted:", dec)