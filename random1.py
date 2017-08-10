#!/usr/bin/env python
import random
tries = 0
rany = random.randint(1, 50)
valx = int(raw_input("Enter a number between 1 and 50::"))
while rany != "valx":
        if valx < rany:
           print "You have entered lower value try again"
	   valx = int(raw_input("Enter a number between 1 and 50::"))
           tries = tries+1
	elif valx > rany: 
	        print "You have entered greater value..try again"
        	valx = int(raw_input("Enter a number between 1 and 50::"))
        	tries = tries+1
	else:
	        tries = tries+1	
        	print "CORRECT, You have done in", tries, "attempts"
        	break
