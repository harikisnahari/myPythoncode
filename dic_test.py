#!/usr/bin/env python
dic1={}
num=int(raw_input("Enter a value :"))
sqr=0
while  num != 0:
	sqr=num**2
	dic1[num]=sqr
	num=int(raw_input("Enter a value :"))

print dic1	
