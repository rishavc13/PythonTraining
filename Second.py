import numpy as np
print("Enter the elements for the matrix:")
a=[int(i) for i in input().split()]
l=len(a)
c=0
factors=[]
for j in range(2,(l//2)+1):
	if(l%j==0):
		c=c+1
		factors.append(j)
if(c==0):
	print("Enter one more element :")
	x=int(input())
	a.append(x)
	l=l+1
	for m in range(2,(l//2)+1):
		if(l%m==0):
			c=c+1
			factors.append(m)
print("Select the order of the matrix from the following available choice(s) :-")
b=0
d=dict()
for k in factors:
	b=b+1
	d.update({b:k})
	print(b,". (",k,',',(l//k),") ")
ch=int(input("Enter your choice :"))
ar=np.array(a)
print(ar.reshape(d[ch],l//d[ch]))
