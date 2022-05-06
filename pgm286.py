# diaplay the file page by page
f=open('pgm282.py','r')
t=f.readline()
n=int(input('n=?'))
x=1
while(n!=0):
     print(x,t,end='')
     if x%10==0:
      n=int(input('n=?'))
     t=f.readline()
     x+=1
f.close()