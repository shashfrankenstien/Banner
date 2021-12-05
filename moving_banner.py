#!/usr/bin/python

__version__ = "3.0.0"

import os, time
import pyfiglet
import argparse

TERM_WIDTH, _ = os.get_terminal_size()

parser = argparse.ArgumentParser(
	"Banner",
	usage="python {} [options] <message>".format(os.path.basename(__file__)),
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument("message", help="message to print as banner", type=str, default=None)
parser.add_argument("--figlet", "-f", help="select figlet font name", type=str, default="banner")
parser.add_argument("--figlet-list", "-fl", help="list available figlet fonts", action="store_true")
parser.add_argument("-x", help="horizontal wall character", type=str, default='_')
parser.add_argument("-y", help="vertical wall character", type=str, default='|')
parser.add_argument("--width", "-w", help="width of the banner", type=int, default=TERM_WIDTH)
parser.add_argument("--speed", "-s", help="speed of the banner", type=int, default=50)
parser.add_argument("--quiet", "-q", help="don't print extra text", action="store_true")


def clear_scr():
	os.system('cls' if os.name == 'nt' else 'clear')


def moving_banner(args):
	if args.message is None:
		parser.print_help()
		exit(1)

	v_char = args.y
	h_char = args.x
	speed = 1/args.speed
	width = max(min(args.width, TERM_WIDTH), 10)
	h_chars_all = h_char * int((width)/len(h_char))
	width -= (2*len(v_char)) + 2 # reducing width to make room for extra characters

	extras = 'Banner! v{}\nPress Ctl+C to exit!'.format(__version__)

	try:
		fig = pyfiglet.Figlet(font=args.figlet)
	except pyfiglet.FontNotFound as e:
		raise Exception("Figlet font {} not found. Use --figlet-list/-fl option to see available fonts".format(args.figlet)) from e
	# convert out to list containing rows of printable characters
	out = [o for o in fig.renderText(str(args.message)).split("\n") if o.strip() != ""]
	clear_scr()

	prefix = " "*width
	while True:
		for offset in range(width+len(out[0])):
			clear_scr()

			print(h_chars_all)
			print(v_char, " "*width, v_char)

			for row in out:
				printString= (prefix+row)[offset:][:width]
				if len(printString) < width:
					printString = printString+(" "*(width-len(printString)))
				print(v_char, printString, v_char)

			print(h_chars_all)
			if not args.quiet:
				print(extras)
			time.sleep(speed)


if __name__=='__main__':
	args = parser.parse_args()
	if args.figlet_list:
		for f in pyfiglet.FigletFont.getFonts():
			print(f)
	else:
		try:
			moving_banner(args)
		except KeyboardInterrupt:
			print("Exit!")
		except Exception as e:
			print(e)
