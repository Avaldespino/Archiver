#! /usr/bin/python3
import os,re,sys
    
def archive(filename):
    bytelist = []
    output = []
    
    
    

        
    #for char in filename.encode():
       # bytelist.append(bin(char))

        
    for i in open(filename, 'rb').read():
        bytelist.append(bin(i))

        
    output.append((bin(len(bytelist))))
    for char in bytelist:
        output.append(char)

    return output





def unarchive(byteList):
    filelength = int(byteList[0],2)
    print(filelength)
    
    f = open("out.txt","w")
    for i in byteList[1:filelength]:
        f.write(chr(int(i,2)))
    

byteArray = archive("file1.txt")   

unarchive(byteArray)
#test = "Hello world"

#test_output = test.encode()
#byteList = []
#for char in test_output:
#byteList.append(bin(char))

#print(byteList)


#for byte in byteList:
    #print('%x' % int(byte,2)).decode('hex').decode('utf-8')

    #print ('%x' % int(byte, 2)).decode('hex').decode('utf-8')
    #print(chr(int(byte,2)))
