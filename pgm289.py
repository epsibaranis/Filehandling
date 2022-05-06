# print the file along with the line number, no of words, no of characters and the text

f=open('pgm282.py','r')
i=0
for x in f:
    i+=1
    l=x.split()
    w=len(l)
    c=len(x)
    print(i,w,c,x,end='')
f.close()
    