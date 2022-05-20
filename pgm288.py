# read a file line by line and print it using for loop
f=open('pgm282.py','r')
for x in f:
    print(x,end='')
f.close()