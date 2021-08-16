# Smoke and Mirrors (39 Solves; 241 Points)
Category: Misc
> A binary file - flag - has been hidden in image.png via LSB-Steganography! It is known that flag is 11,392 bytes large. Also, the file is spread across the first N pixels of the image when traversing in row-major order.
> 
> Can you recover the executable and uncover the flag?

In this challenge, we are expected to retrieve the data that is hidden within the image via steganography.

Since the steganography scheme is made known to us, the only work we have to do is to reverse the scheme.

In LSB-Steganography, the data is every least significant bit (LSB) of every byte of the image.


Together with the knowledge about the size of the flag executable, we can just read the LSBs up to the size of the flag, concatenate them and write them to a file to be executed.

To read the image, the `imageio` python package can be used.
Using this to read the image would produce a 2D array.

After this, the only work left is to iterate through all the bytes and extract the LSB.
Once the correct number of bits is read, the data is then written to another file.

Executing the file gives us the flag
> greyhats{m0r3_th6n_m33t5_the_3y3_189794872}