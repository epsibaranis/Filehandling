#read and diaplay line by line at the end of the file

f=open('pgm250.py','r')
t=f.readline()
while(t):
     print(t,end='')
     t=f.readline()
f.close()