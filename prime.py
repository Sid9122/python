#!/usr/bin/python3

ctr=0
num=int(input("Enter a number"))
for i in range(1,num+1): 
#	print(i)
	if num%i==0:
		ctr=ctr+1
if ctr==2:
	print("it is a prime number")
else:
	print("it is not a prime number")
	ctr=0
	

