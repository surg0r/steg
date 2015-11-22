# steg
bitcoin steganography library

Hide a bitcoin private key in an image file..

dependencies bitcoin (pybitcointools), PIL
(sudo pip install bitcoin, sudo pip install PIL)

The steg.py file has a single class to instantiate Steg():
It contains two functions, encode and decode:

encode(file, data) 
takes data string (e.g. private key) as an argument and inserts it into the image file by altering the least significant bit of the R palette value from the r,g,b tuple of each consecutive pixel until the data is inserted.
To convert a hexadecimal random private key representation to a wif format key you may call the function
wif_private_key(key).
The string is encoded with a 4 byte sha256(data) checksum appended and a string length byte prepended.

data = decode(optional file arg)
By default opens output.png but can be overridden by supplying different name.
It returns the decoded string and confirms data integrity by checksum.

Improvements..

1) implement redundancy so that a lossy output file (with compression such as a jpg) can be used as opposed say a png or other lossless medium..
