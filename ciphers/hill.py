text = input("Enter text: ").upper()   #text should be of even length or add x

k = [[3,3],
     [2,5]]

enc =""
for i in range(0,len(text),2):
    p1 = ord(text[i]) - 65
    p2 = ord(text[i+1]) - 65

    c1 = (k[0][0]*p1 + k[0][1]*p2) %26 + 65
    c2 = (k[1][0]*p1 + k[1][1]*p2) %26 + 65

    enc += chr(c1)+chr(c2)
print("Encrypted: ",enc)    