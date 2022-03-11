#! /usr/bin/python3
import os,re,sys

if len(sys.argv) == 1:
    os.write(2, ("No files are given\n").encode())
    sys.exit(1)
name = str(sys.argv[1])
out = name.split('.')
out = out[0]+".arch"
fileOut = os.open(out, os.O_CREAT | os.O_WRONLY)

for i in range(1,len(sys.argv)):
   with open(sys.argv[i], 'r') as f:
      contents = f.read()
   byteList = []   
   for char in contents.encode():
       byteList.append(bin(char)
   
   os.write(fileOut, byteList)
   
               
#test = "Hello world"

#test_output = test.encode()
#byteList = []
#for char in test_output:
 #   byteList.append(bin(char))

#print(byteList)


#for byte in byteList:
    #print('%x' % int(byte,2)).decode('hex').decode('utf-8')

    #print ('%x' % int(byte, 2)).decode('hex').decode('utf-8')
 #   print(chr(int(byte,2)))
