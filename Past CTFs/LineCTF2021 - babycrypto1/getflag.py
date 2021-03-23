##https://dystopia.sg/linectf21-babycrypto1/
'''
learnt: how does CBC mode work

idea: exploit weakness in CBC mode,
where payload aligns with the block margin, and provided with encryption oracle (with IV and cipher)

=> send second last chunk as IV, and plaintext payload as plaintext
=> replace last chunk with poisoned chunk

issues faced:
* increase familiarity with code. Correct payload, but did not read enough to read the flag
'''
from pwn import *
from Crypto.Cipher import AES
from base64 import b64decode
from base64 import b64encode

r = remote('localhost', 16001)

def chunkify(payload, blocksize):
    output = []
    while payload:
        output.append(payload[:blocksize])
        payload = payload[blocksize:]
    return output

r.recvuntil("test Command: ")
ciphertext = b64decode(r.recvline())
ciphertext = chunkify(ciphertext, AES.block_size)
IV = ciphertext[-2]
#print(IV)

r.recvuntil("IV...: ")
r.sendline(b64encode(IV))

r.recvuntil("Message...: ")
r.sendline(b64encode(b"show"))

r.recvuntil("Ciphertext:")
temp = b64decode(r.recvline().rstrip())


r.recvuntil("Enter your command: ")
poison_ciphertext = ciphertext[:-2] + [temp, ]
r.sendline(b64encode(b''.join(poison_ciphertext)))
print(r.recv(1024))
print(r.recv(1024))
