#! /usr/bin/python3
import os,re,sys

if len(sys.argv) == 1:
    os.write(2, ("No files are given\n").encode())
    sys.exit(1)
name = str(sys.argv[1])
fileOut = os.open(name, os.O_CREAT | os.O_WRONLY)

for i in range(2,len(sys.argv)):
   with open(sys.argv[i], 'r') as f:
      contents = f.read()
   byteContents = contents.encode()
   size = str(len(byteContents)).encode()
   output = size+byteContents
   output = output.bytearray()
   os.write(fileOut, output)
   
               
test = "Hello world"

byte = test.encode()

print(byte)
