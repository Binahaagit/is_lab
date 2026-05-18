import hashlib

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

h1 = hashlib.sha256(s1.encode()).hexdigest()
h2 = hashlib.sha256(s2.encode()).hexdigest()

print("Hash 1: ",h1)
print("Hash 2: ",h2)

x = int(h1,16) ^ int(h2,16)

print("Different bits: ", bin(x).count('1'))