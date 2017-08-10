#!/usr/bin/env python
n = int(input("Enter till which number you want to see prime numbers: "))
list1=[]
for prm in xrange(2,n+1):
	chk=0
   	for i in xrange(2,prm):
       	       if prm % i == 0:
        	         	chk=chk+1 
	if chk == 0:
			list1.append(prm)

print list1
