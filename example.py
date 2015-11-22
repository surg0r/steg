#Example script using steg.py which inserts a private key into a supplied image and outputs output.png containing the key

__author__ = 'pete'
from steg import *

print 'Bitcoin steganography tool..example'
print '>>>Usage: type or paste the path and filename of an image file to be used: '
img_file = raw_input()
if not img_file:
    print 'this only works with a provided image file - sorry'
    exit()

st = Steg()     #instantiate the steg class

print '>>>Usage: now type or paste a private key to encode into the image (hit enter for a random key to be generated):'
priv = raw_input()
if not priv:
    priv = random_key()
print 'hex', priv
priv = create_wif_key(priv)
print ' input', priv

st.encode(img_file, priv)          #encode key
data = st.decode('output.png')        #decode key

print 'output', data
