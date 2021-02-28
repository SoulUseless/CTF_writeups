
def euclid_algo(x, y):
    if x < y: 
        return euclid_algo(y, x)
    while y != 0:
        (x, y) = (y, x % y)
    return x

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def isPrime(n) : 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

'''
PRP2 = []
for i in range(1,50):
    x = 2 ** (i - 1)
    if x % i == 1:
        PRP2.append(i)
##print(PRP2)

##print("prp check done")
prime = 0
for i in PRP2:
    #print(i)
    if isPrime(i):
        prime += 1

##print(prime)
##print(len(PRP2))
##print(prime / len(PRP2) * 100)

possible = []
for i in range(1, 80):
    lcm = compute_lcm(10, 16)
    if euclid_algo(i, lcm) == 1:
        for j in range(1, 80):
            if i * j % lcm == 1:
                possible.append((i, j))

print(possible)


i = 1
while True:
    i += 160
    if i % 29 == 0:
        print(i // 29)
        break


i = 2 ** (283 * 12345)
print(i)
while i > 738821:
    i -= 738821
print(i)


import math
i = 1
while True:
    test = 152 ** i
    print(pow(169, i, 187))
    i += 1

'''

import random
import math
possible_seed_values = []

def generate_prp(length):
    for i in range(10 ** (length - 1), 10 ** length - 1):
        x = 2 ** (i - 1)
        if x % i == 1:
            possible_seed_values.append(i)

generate_prp(3)
print(possible_seed_values)

m = possible_seed_values[random.randint(0, len(possible_seed_values) - 1)]                  
n = possible_seed_values[random.randint(0, len(possible_seed_values) - 1)]
lcm = compute_lcm(m - 1, n - 1)
print(m,n)
possible_keys = []

for i in range(1, lcm):
    if euclid_algo(i, lcm) == 1:
        for j in range(1, lcm):
            if i * j % lcm == 1:
                possible_keys.append((i, j))
        #print(i)

priv_pub_key = possible_keys[random.randint(0, len(possible_keys) - 1)]
print(priv_pub_key)
priv = priv_pub_key[0]
pub = priv_pub_key[1]

message = 12

#encrypt
cipher = pow(2, pub * message, m * n)
print(cipher)

#decrypt
plaintext = math.log(pow(cipher, priv, m * n), 2)
print(plaintext)
