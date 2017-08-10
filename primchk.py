#!/usr/bin/env python
n = int(input("Enter till which number you want to see prime numbers: "))
list1=[2]

if n > 1:
	for prm in xrange(2,n+1):
#			        print prm,"prm in first loop"
	   			for i in xrange(2,prm):
#	 				print i,"i in second loop"
       					if prm % i == 0:
        	  				 break
       					else:
				#		list1.append(prm)
						print prm
else:
  print "Enter number greater than 1"

#print list1
