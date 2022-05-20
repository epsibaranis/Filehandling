# Bring the file along with the line number
f=open('pgm282.py','r')
t=f.readline()
n=int(input('n=?'))
x=1
while(n!=0):
     print(x,t,end='')
     t=f.readline()
     x+=1
f.close()