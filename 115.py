n,k=map(int,input("N and K").split(' '))
a=[]
for i in range(0,n):
 b=int(input("numbers"))
 a.append(b)
b=sorted(a)
print(b[k-1])
