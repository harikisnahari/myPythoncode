#!/usr/bin/env python
n = int(input("Enter till which number you want to see prime numbers: "))
dicprime={}
prmchk=0
for prm in xrange(2,n+1):
	chk=0
   	for i in xrange(2,prm):
       	       if prm % i == 0:
        	         	chk=chk+1 
	if chk == 0:
			prmchk=prmchk+1
			dicprime[prmchk]=prm

#print dicprime
count=len(dicprime.values())
print "Total number of Prime numbers found are ",count
print "Give the Iteration number you want to see the prime number at"
val=int(raw_input())
getval=dicprime.get(val)
print "Prime number at ",val ,"is ",getval 
