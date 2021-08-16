import imageio
im = list(imageio.imread("C:/Users/jkyap/Desktop/ctf/greyhat/image.png"))

bits = ""
for row in im:
    bits += "".join(list(map(lambda x:str(x % 2), row)))
    if len(bits) > 11392 * 8:
        break

bits = bits[:11392 * 8]
bits = int(bits, 2)
b = bytearray()
while bits:
    b.append(bits & 0xff)
    bits >>= 8
b = bytes(b[::-1])

with open("test", "wb") as f:
    f.write(b)
    f.close()
