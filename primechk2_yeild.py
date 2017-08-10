#!/usr/bin/env python
def primechk(n):
	primelst=[]
	prmchk=0
	for prm in xrange(2,n+1):
        	chk=0
        	for i in xrange(2,prm):
               		if prm % i == 0:
                                chk=chk+1
        	if chk == 0:
                        prmchk=prmchk+1
                        primelst.append(prm)
			yield prm
	#yield primelst




num = int(input("Enter till which number you want to see prime numbers: "))
x=primechk(num)
#print x
#list1=[]
#for i in xrange(0,num-1):
#	print i
	#list1.append(x.next())
print x.next()
