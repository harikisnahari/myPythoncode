#!/usr/bin/env python
import random
tries = 1
rany = random.randint(1, 50)
valx = int(raw_input("Enter a number between 1 and 50::"))
if valx > 50 or valx < 0:
  print "Dont act smart.. entr between 1 and 50 ONLY...MAIN"
  valx = int(raw_input("Enter a number between 1 and 50::"))
else:
     while rany != "valx":
        if valx < rany:
           print "You have entered lower value try again"
	   valx = int(raw_input("Enter a number between 1 and 50::"))
	   if valx > 50 or valx < 0:
		  print "Dont act smart.. entr between 1 and 50 ONLY .. in v<r"
  		  valx = int(raw_input("Enter a number between 1 and 50::"))
           tries = tries+1
	elif valx > rany: 
	        print "You have entered greater value..try again"
        	valx = int(raw_input("Enter a number between 1 and 50::"))
		if valx > 50 or valx < 0:
                   print "Dont act smart.. entr between 1 and 50 ONLY... in v>r"
                   valx = int(raw_input("Enter a number between 1 and 50::"))
        	tries = tries+1
	else:
        	print "CORRECT, You have done in", tries, "attempts"
        	break
