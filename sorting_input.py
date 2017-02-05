##hey there,
## here i am tryong to sort aa list, in o(n) time in variant of the randomness of the 
## element sin the list or array.
## i took the example of a list here but the logic is eqully applicable for an array too.
## here i am goint to read a list of positive real integers of any in any random order. 
## and put them in a new list with their index as the same value as the element being read in the list
## Well obviously for the big numbers there will be space complexity because of the size of the new extra 
## list being created. But it will be very effective for small numbers.
## later i would like to test the effeciecy of the method by passing same order of integers to differnet sorting methods
## that are available right now, including radix sort. that i think sounds similar to what i am trying to do.
## so lets do it.

## lets first create a list of random integers.
## lets say for the sake of my system, although i keep in mind the space complexity in this method,
## the max size of the integer in the list be 200 right now.

# import randint from "random" module.
from random import randint as itsrandom
from time import time

# initialize a zero length list, that will store the integers.
# this part can also be skipped if the user wants to input each number sindividually in a loop and 
# desires for a sorted order in the end of the program.
# anyways!
#---------------------LOGIC--------------------------#
#	for each input, start appending the occurance of str(integer) to the string
#	at the index of the integer. If the integers in the input are not in a 
#	consecutive order, eg. 1,2,5,7; leave the position to be empty.
#	To check multiple occurance of an integer, keep the integer in a list,
#	if its not in the list, else increase the count for that integer
l=[]

# run a loop to append numbers in the list
while len(l)<1000:
	n=itsrandom(0,200)
	print n,
	l.append(n)

start = time()
r={"0":0}	# initializing a dictory that stores the intger in string format as the key and the occurance in intger format as it's value.
s=""
for i in l:
	# just to avoid the hassle of repeating str(i) almost everywhere in the code.
	int_to_str=str(i)

	#check if the integer has not already occured.
	if not int_to_str in r.keys():
		#setting the initial occurance to be 1.
		r[int_to_str]=1
		#checking if the string s has length less than the integer, for later the occurance of the integer will be added at the index=integer 
		if i>len(s):
			## Increasing the length of the string so that size is equal to the integer. 
			s+="0"*(i-len(s)-1)+str(r[int_to_str])
		else:
			s=s[:i]+str(r[int_to_str])+s[i+1:]
	else:
		r[int_to_str]+=1
		if i==len(s):
			s=s[:i]+str(r[int_to_str])
		else:
			s=s[:i]+str(r[int_to_str])+s[i+1:]
mid_time= time()-start
result = ""
for i in xrange(len(s)):
	result += (str(i)+" ")*int(s[i])
end = time()-start
print result[:-1].split()
print r
print mid_time, end