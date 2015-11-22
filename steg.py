#Bitcoin steganography library, inserts a private key, wif by default into a named file by altering the LSB of the r
#in the rgb palette of the pixel.
#Hex bitcoin private key is 64 bytes (512 bits to hide)
#WIF bitcoin private key is 51 bytes (408 bits to hide) and easily importable into a wallet for sweeping..

__author__ = 'pete'
from bitcoin import *                      #probably just need encode_privkey() and random_key()
from PIL import Image

class Steg_in():                           #instantiate a class which allows steganography data in and out of im..
    def __init__(self, file):
        self.im = Image.open(file)
        self.im_w, self.im_h = self.im.size
        self.rgb_im = self.im.convert('RGB')

    def steg_in(self, data, output='output.png'):            #put data into image..
        self.output = output
        self.data = data
        self.datalen = len(self.data)   #number of bytes
        self.bitcount = self.datalen * 8    #number of bits in bytestring to disguise
        s  = []

        for x in range(0,self.datalen):     #convert the data into an ascii bit list.
            p = bin(ord(self.data[x]))
            p = p.lstrip('-0b')
            while len(p) < 8:               #pad the zero's up to 8
                p = '0'+ p
            s.append(p)
        s = "".join(s)                  #list to string

        if self.bitcount < self.im_w:               #can fit the entire message in first row of pixels..
            for x in range(0,self.bitcount):
                r, g, b = self.rgb_im.getpixel((x,0))       #get the pixel in r,g,b form..
                r = r & 254                                 #and 11111110
                if s[x] == '1':
                    r = r | 1                               #or 00000001
                self.rgb_im.putpixel((x,0),(r,g,b))         #put the replaced pixel with LSB altered..
        self.rgb_im.save(self.output)

    def create_wif_key(self, key):
        return encode_privkey(key, 'wif')

class Steg_out():                               #instantiates a class which allows data out..
    def __init__(self, file='output.png'):
        self.im = Image.open(file)
        self.im_w, self.im_h = self.im.size
        self.rgb_im = self.im.convert('RGB')

    def steg_out(self,n=408):         #n=512 (64 hex * 8), n=408 (64 hex -> 51 wif * 8) extract private key from file..
        self.bitlength = n
        t  = []
        j = 0
        for x in range(0,(self.bitlength / 8)):     #convert the ascii bit string back to ascii integer string
            p=""
            for y in range(0,8):
                r, g, b = self.rgb_im.getpixel((j,0))
                r = r & 1
                p = p + str(r)
                j += 1
            t.append(chr(int(p,2)))
        t = "".join(t)
        return t

