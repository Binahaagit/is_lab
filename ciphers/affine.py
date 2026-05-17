text = input("Enter text: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

enc =""
for ch in text:
    enc += chr((a*(ord(ch)-65)+b)%26 + 65)
print("Encrypted: ",enc)

#multiplicative inverse
for i in range(26):
    if(a*i)%26 == 1:
        a_inv = i

dec =""
for ch in enc:
    dec += chr((a_inv*(ord(ch)-65-b))%26 + 65)
print("Decrypted: ",dec)