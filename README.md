# steg
bitcoin steganography library

Hide a bitcoin private key in an image file..

dependencies bitcoin (pybitcointools), PIL
(sudo pip install bitcoin, sudo pip install PIL)

The steg.py file has a single class to instantiate Steg( ):
It contains two functions, encode and decode:

Example: 

to encode an image file with a string such as a private key

encode(inputfile, data, outputfile)

1. instantiate the class
steg = Steg()
2. encode the file with a string
st.encode('image_I_want_to_use.jpg','string or private key I want to encode','output_file_I_want_to_use.png')

Encode takes data string (e.g. private key) as an argument and inserts it into the image file by altering the least significant bit of the R palette value from the r,g,b tuple of each consecutive pixel until the data is inserted.
To convert a hexadecimal random private key representation to a wif format key you may call the function
wif_private_key(key). The string is encoded with a 4 byte sha256(data) checksum appended and a string length byte prepended. Outputfile defaults to 'output.png' if not provided.

Example:

to decode an string from an image file

hidden_string_or_key = decode('optional file arg')

By default opens output.png but can be overridden by supplying different name.
It returns the decoded string after confirmation of data integrity by sha256 checksum.

Improvements, issues..

1) implement redundancy so that a lossy output file (with compression such as a jpg) can be used as opposed say a png or other lossless medium..

2) you must test output to a lossy output image format as this likely will not work yet..png is safe
