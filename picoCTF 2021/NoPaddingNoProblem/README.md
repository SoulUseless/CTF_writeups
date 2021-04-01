# No Padding, No Problem (90 Points)
Category: Cryptography
> Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it?

In this challenge, we were required to connect to a remote host, which will give us the public key (e, N), the ciphertext, and provide us with a decryption oracle.

Originally, I did not have much idea where to start, until I chanced upon a very helpful StackExchange [page](https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack), 
that was actually about a more specific version of an oracle attack.
I found this quote:
> If an attacker intercepts an encrypted plaintext 
> <img src="https://render.githubusercontent.com/render/math?math=c = P^e mod N">
> he could multiply it by
> <img src="https://render.githubusercontent.com/render/math?math=2^e mod N">
> (essentially doubling the original plaintext) and send it to the oracle.

This gave me the insight and launching off point for this challenge.

From the abstract, from how RSA works deterministically, if we pass in a ciphertext that is 2 (arbitrarily chosen) times the original ciphertext, the decryption oracle should spit out 2 times the plaintext.

With this understanding, `test.py` was created.

This challenge was also the first challenge that I scripted something that connects to a remote host and automatically prints the flag out for me using pwntools.

<img src="flag.png" />

## Learning Points
* Learnt and understood about the deterministic nature of textbook RSA
* Learnt the basic uses of `pwntools` in the context of CTF and remote host connection