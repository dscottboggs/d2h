#!/bin/python

#hex - dec converter
import sys
DEBUG=0		#debug var
HighOrder={		#this is a python "dictionary", their stupid thing instead of switch-case.
	10:'A',		#	This handles replacing 10-15 with A-F for hex notation
	11:'B',
	12:'C',
	13:'D',
	14:'E',
	15:'F'
		}
finalresult=""	#initialize this var as a string
def main():			#CALLED FROM LINE 46!!		!!!
	try:						#check for an argument
		numIn=int(sys.argv[1])	#save the arg as the input variable
	except:						#if there wasn't an argument passed to the system
		print("Hex 2 Dec -- usage -- h2d <value>\nBe sure to include a decimal value to convert!")
		exit(1)					#print usage instructions and exit.
	result=reduction(numIn)		#	!!	this calls the actual algorithm to get hex results @line 26
	print(result)				# 		and prints it
	
def default(d):		#the "defualt" case in pythons stupid fake switch-case
	return d		#and simply returns any value passed to it
def reduction(i):				#the core of the script
	numIn=i						#set the value passed to the method as an input variable (technically optional)
	result=numIn//16			#get the floor division value of the input to this iteration of the method by 16
	remainder=numIn%16			#and the remainder
	if(result==0):				# if the floor-division result is zero, you have base-case
		if DEBUG: print(str(numIn) + ", " + str(remainder))
		try:
			remainder=HighOrder[remainder]	#first replace all high order values with letters
		except KeyError:
			remainder=default(remainder)	# and keep the low-order values the same by calling the method @ line 24 when a value is not found in the "dictionary" or switch-case statement
		return str(remainder)		# then make the base-case return
	else:						# if floor division results in something other than ZERO,
		if DEBUG: print(str(numIn) + ", " + str(remainder))
		try:
			remainder=HighOrder[remainder]	# (you still have to convert high order stuff to letters)
		except KeyError:
			remainder=default(remainder)
		finalresult=reduction(result)+str(remainder)	# recursively call this method with the result of floor division, then add the string-ized
														#	remainder to the result of the recursive reduction
		return(finalresult)					# and return what you've received. 
	
main()		#	call the main method at line 15
