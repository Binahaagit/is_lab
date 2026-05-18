from sympy import gcd, mod_inverse
import hashlib

p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p*q
phi= (p-1)*(q-1)

e = int(input("Enter e: "))
#or generate list of possible e values using gcd as in rsa and choose one 
d=mod_inverse(e,phi)

m = input("Enter message: ")
h =int(hashlib.sha256(m.encode()).hexdigest(),16)
print("Hash: ",h)

sign = pow(h,d,n)
print("Signature: ",sign)

verify = pow(sign,e,n)

if verify == h%n :
    print("signature valid")
else:
    print("signature invalid")

