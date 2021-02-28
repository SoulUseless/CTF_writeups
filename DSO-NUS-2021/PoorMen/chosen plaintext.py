import math

data = ""
with open ("data.txt", "r") as f:
    data = f.read()
    f.close()

pks = []
ciphers = []

pubkeys, cs = data.split("cs: ")
pubkeys = pubkeys[11:-3]
cs = cs[1:-1]

pubkeys = pubkeys.split("), (")
for pk in pubkeys:
    e, N = pk.split(", ")
    pks.append((int(e), int(N)))
print("pk done")

cs = cs.split(", ")
for cipher in cs:
    c = int(cipher)
    ciphers.append(c)
print("cipher done")

print(ciphers[-1])
print(len(pks))
print(len(ciphers))

def encrypt(e, N, plaintext):
    return pow(2, e*plaintext, N)

result = ""

for i in range(len(pks)):
    e = pks[i][0]
    N = pks[i][1]
    c = ciphers[i]

    j = 1
    max = math.log(N, 2)
    while j < max:
        if encrypt(e, N, j) == c:
            result += chr(j)
        j += 1
    print(result)

print(result)
