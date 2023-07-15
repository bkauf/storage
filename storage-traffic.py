#!/usr/bin/python
import time

#time.sleep(2.4)
while True:
    time.sleep(2.4)
    for i in range(5):
        print(i, end=", ") # prints: 0, 1, 2, 3, 4, 
        # Open a file
        filename = str(i)
        fo = open(filename+".txt", "w")
        fo.write("Woops! I have deleted the content!")

        #fo = open("foo.txt", "r+")
        #str = fo.read(1)
        #print("Read String is : ", str)
        # Close opend file
        fo.close()