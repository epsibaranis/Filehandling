# print the line that derivess the highest no.of characters file in the dictionary
f=open('pgm282.py','r')
d={}
i=0
b=0
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
for x in d:
    if b<d[x][2]:
        b=x
print(d[b])
f.close()