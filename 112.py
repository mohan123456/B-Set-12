n,k=map(int,input("N and K").split(' '))
a=[]
for i in range(0,n):
 b=int(input("numbers"))
 a.append(b)
for i in a:
  if (i == k):
    print("yess")
    break
else:
    print("noo")  
