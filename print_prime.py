#! /usr/bin/python3

num=int(input("Enter range"))
for i in range(1,num+1):
	ctr=0
	for j in range(1,i+1):
		if i%j==0 :
			ctr=ctr+1
	if ctr==2:
		print(i)
	ctr=0
