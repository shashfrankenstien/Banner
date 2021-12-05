#!/usr/bin/python

__version__ = "2.0.0"

import os, time
from alphabet import alphabet, alphabet_char
import argparse

TERM_WIDTH, _ = os.get_terminal_size()

parser = argparse.ArgumentParser("python {}".format(os.path.basename(__file__)))
parser.add_argument("message", help="message to print as banner")
parser.add_argument("-c", help="character used for banner text", type=str, default=alphabet_char)
parser.add_argument("-x", help="horizontal wall character", type=str, default='_')
parser.add_argument("-y", help="vertical wall character", type=str, default='|')
parser.add_argument("--width", "-w", help="width of the banner", type=int, default=TERM_WIDTH)
parser.add_argument("--speed", "-s", help="speed of the banner", type=int, default=50)
parser.add_argument("--quiet", "-q", help="don't print extra text", action="store_true")

def clear_scr():
	os.system('cls' if os.name == 'nt' else 'clear')

def convert(message, replace_char):
	output = []
	for i in range(7):
		outputTemp=''
		for char in str(message).upper():
			outString = alphabet[char][i]+"  "
			if replace_char and replace_char != alphabet_char:
				outString = outString.replace(alphabet_char, str(replace_char)[0])
			outputTemp += outString
		output.append(outputTemp)
	return output

def moving_banner():
	args = parser.parse_args()
	v_char = args.y
	h_char = args.x
	speed = 1/args.speed
	width = min(args.width, TERM_WIDTH)
	h_chars_all = h_char * int((width)/len(h_char))
	width -= (2*len(v_char)) + 2 # reducing width to make room for extra characters

	extras = 'Banner! v{}\nPress Ctl+C to exit!'.format(__version__)

	out = convert(args.message, args.c)
	clear_scr()

	prefix = " "*width
	while True:
		for offset in range(width+len(out[0])):
			clear_scr()

			print(h_chars_all)
			print(v_char, " "*width, v_char)

			for row in range(7):
				printString= (prefix+out[row])[offset:][:width]
				if len(printString) < width:
					printString = printString+(" "*(width-len(printString)))
				print(v_char, printString, v_char)

			print(h_chars_all)
			if not args.quiet:
				print(extras)
			time.sleep(speed)


if __name__=='__main__':
	try:
		moving_banner()
	except KeyboardInterrupt:
		print("Exit!")
	except Exception as e:
		print(e)

