# print the file in the dictionary  along with the line number, no of words, no of characters and the text
f=open('pgm282.py','r')
d={}
i=0
for x in f:
    a=[]
    i+=1
    l=x.split()
    w=len(l)
    c=len(x)
    a.append(w)
    a.append(c)
    a.append(x)
    d[i]=a
print(d)
f.close()