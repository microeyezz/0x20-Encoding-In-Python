#!/usr/bin/python -tt
import random

def check_en():
	indexes = set()
	encode = []
	url = raw_input("Enter URL: ")
	i = 0
	for s in url:
		if s.isupper():
			encode.append(0)
		elif s.islower():
			encode.append(1)
			
	print "value of l is: ",len(url)
	
	#print random.randrange(1024, 65535, 1)
	rand_port = random.randint(1024,65535)
	rand_num = random.randint(10000,90000)
	print "Random number is:",rand_num
	print "Random port is:",rand_port

	bin_val =  bin(rand_port)
	print "binary value of port : ",bin_val[-len(url):]

	bin_num = bin(rand_num)
	print "binary value of port : ",bin_num[-len(url):]

	
	
	final_key = int(rand_port) ^ int(rand_num)
	bin_fin_key = bin(final_key)
	fin_key_fin = bin_fin_key[-len(url):]
	print "Final Key is: ",fin_key_fin 
	index = 0

	while index < len(fin_key_fin):
        	index = fin_key_fin.find('1', index)
		
		if index == -1:
			break
		indexes.add(index)
    		print('1 found at', index)

		index = index + 1
		
		
		
		
	chars = list(url)
	for i in indexes:
    		chars[i] = chars[i].upper()		
	string = ''.join(chars)

	print "0x20 Encoded URL is: ",string
			
	
	

def main():
	check_en()
	
	

if __name__ =='__main__':
	main()

			
