import os, time
from alphabet import alphabet

message = raw_input("Enter something - ")
message = message.upper()

def convert(message):
	output = []
	for i in range(7):
		outputTemp=''
		for char in message:
			outString = alphabet[char][i]+"  "
			outputTemp += outString
		output.append(outputTemp)
	return output

def moving_banner(out):
	os.system('clear')
	length = 100
	speed = 0.05
	start = [(i+1) for i in list(reversed(range(length)))]
	exit = [(i+1) for i in list(reversed(range(len(out[0]))))]
	for offset in start:
		os.system('clear')
		for row in range(7):
			print (" "*offset+out[row])[:length]
		time.sleep(speed)
	for red in exit:
		os.system('clear')
		for row in range(7):
			print out[row][-red:length]
		time.sleep(speed)



if __name__=='__main__':
	output = convert(message)
	while True:
		moving_banner(output)






# print '\n'
# for row in output:
# 	print row
# print '\n'








