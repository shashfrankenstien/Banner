#!/usr/bin/python

import os, time
from alphabet import alphabet



def convert(message):
	output = []
	for i in range(7):
		outputTemp=''
		for char in message:
			outString = alphabet[char][i]+"  "
			outputTemp += outString
		output.append(outputTemp)
	return output

def moving_banner(out, speed=0.1, length=50):
	os.system('clear')
	start = [(i+1) for i in list(reversed(range(length)))]
	exit = [(i+1) for i in list(reversed(range(len(out[0]))))]

	prefix = " "*length
	for offset in range(length+len(out[0])):
		os.system('clear')

		print "_"*(length+4)
		print '|', " "*length, '|'

		for row in range(7):
			printString= (prefix+out[row])[offset:][:length]
			if len(printString) < length:
				printString = printString+(" "*(length-len(printString)))
			print '|', printString, '|'

		print "o"*(length+4)

		print '\nPress Ctl+C to exit!'
		time.sleep(speed)


if __name__=='__main__':
	os.system('clear')
	message = raw_input("Enter something - ")
	message = message.upper()
	output = convert(message)
	while True:
		try:
			moving_banner(output, speed=0.02)
		except: break






# print '\n'
# for row in output:
# 	print row
# print '\n'








