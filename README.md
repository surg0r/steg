# steg
bitcoin steganography library

Hide a bitcoin private key in an image file..

dependencies bitcoin (pybitcointools), PIL
(sudo pip install bitcoin, sudo pip install PIL)

The steg.py file has two classes, Steg_in and Steg_out:

Steg_in()
Steg_in takes a filename arg an image file and it contains the function steg_in(data) which takes data and 
inserts it into the image file by altering the least significant bit of the R palette value from the r,g,b tuple of 
each consecutive pixel until the data is inserted.
To convert a hexadecimal random private key representation to a wif format key then you can call the function
wif_private_key(key)

Steg_out()
This class opens by default output.png but supplying a file alters input image.
It contains the function steg_out() and returns the supplied number of bits of data from the image.
The default setting is to remove 408 bits unless otherwise instructed - this is because a WIF private key is 51 bytes
and 408 bits in length.

Improvements to make:
1) explicit handling of 'hex', 'wif' and 'bip38' keys.
2) implement a checksum on data extraction..
3) implement redundancy so that a lossy output file (with compression such as a jpg) can be used as opposed say a png..
