from pwn import *
from Crypto.Util.number import long_to_bytes
import decimal
decimal.getcontext().prec = 4096

r = remote("mercury.picoctf.net", 33780)

r.recvuntil('\n\n\n')
N = int(r.recvline()[:-1].split(b": ")[1].decode())
E = int(r.recvline()[:-1].split(b": ")[1].decode())
C = int(r.recvline()[:-1].split(b": ")[1].decode())

#print(N)
#print(E)
#print(C)
#print()

##https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack
multiplier = str(C * pow(2, E, N) % N)

print(r.recvuntil('Give me ciphertext to decrypt: '))
r.sendline(multiplier)
x = decimal.Decimal(int(r.recvline()[:-1].split(b": ")[1].decode()))
print(x)
print(long_to_bytes(x/2).decode())

