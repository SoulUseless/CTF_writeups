data = ""

with open ("data.txt", "r") as f:
    data = f.read()
    f.close()

data = data.split("cs: ")[0][9:]
data = data[2:len(data) - 1]
data = data.split("), (")
data = list(map(lambda x: x.split(", ")[1], data))

with open("test.py", "w") as f:
    for pkey in data:
        f.write(pkey + "\n")
    f.close()
