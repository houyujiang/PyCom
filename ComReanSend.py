#_*_coding: utf-8 _*_
import serial
import binascii
s = serial.Serial('com3',115200)
d=bytes.fromhex('68 02 09 00')
print(d)
s.write(d)
argv = s.read(3)
result =""
hlen = len(argv)
for i in range(hlen):
    hvol =ord(argv[i])
    hhex = '%02x'%hvol
    result +=hhex+''
print ('hexshow:',result)

