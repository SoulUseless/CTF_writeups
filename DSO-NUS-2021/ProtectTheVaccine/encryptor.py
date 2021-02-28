from config import a,b,m,r_p,r_q,secret
from Crypto.Util.number import bytes_to_long

p = a**m + r_p
q = b**m + r_q
N = p*q
e = 65537

M = bytes_to_long(secret)
c = pow(M, e, N)

print('N:', N)
print('e:', e)
print('r_p:', r_p)
print('r_q:', r_q)
print('c:', c)
