#! /usr/bin/python3

num=int(input("Enter a number"))

# initializing reverse to 0
rev=0
while(num>0) :
	d=num%10
	rev=(rev*10)+d
	num=num//10
print(rev)


