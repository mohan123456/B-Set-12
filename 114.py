n,k=map(int,input("N and K").split(' '))
a=[]
for i in range(0,n):
 b=int(input("numbers"))
 a.append(b)
c=[]
for i in a:
  if(i%2!=0):
    c.append(i)
print(c[k-1])
