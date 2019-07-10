#!/usr/bin/env python3
# Coded By: A_Asaker

import sys,os
import random
import curses
from time import sleep

def usage():
	print("""\t\t\033[1;91;100m Terminal Effects - By : A_Asaker \033[0m
 [-] Usage: ./term_eff.py [option/s]
 [-] Options: 
	    -t :	cmatrix Effect, [Bottom To Top]
	    -d :	Backgound colors Scrolling
	    -w :	Mixed Colors [For Background Scrolling Colors Effect]
	    -h :	help()
 [-] Key Bindings:
	     w :	Mixed Colors Effect [on/off]
	     d :	Colors Scrolling [on/off]
	     t :	cmatrix Effect[on/off]
	     q/[esc]:	Exit
 [-] Example:
	    ~	./term_eff.py -t
	    ~	./term_eff.py -w -d
""")
	sys.exit(0)

if "-h" in sys.argv:
	usage()
white=0 
func='d' if '-d' in sys.argv else "t"
white = 1 if "-w" in sys.argv else 0
d_color="\033[0m"
stdscr = curses.initscr()
curses.curs_set(0)
f_colors=list(range(30,37))+(list(range(90,97)))
b_colors=list(range(40,47))+(list(range(100,107)))
print("\033[32m")
print('\033[?1049h')
	
def rn(f=32,l=120):
	return random.randint(f,l)

def draw():
	x=rn(1,os.get_terminal_size(0).columns)
	y=rn(1,os.get_terminal_size(0).lines)
	front=f_colors[rn(0,len(f_colors)-1)]
	back =b_colors[rn(0,len(b_colors)-1)]
	print("\033[{};{}H{}\033[{};{}m".format(y,x,(white and rn(1,10))*" ",front,back))
	print("\033[{};{}H{}\033[{};{}m".format(y+5,x,(white and rn(1,10))*" ",f_colors[rn(0,len(f_colors)-1)],back))
	sys.stdout.flush()
	stdscr.timeout(10)

def cmat():
	x=rn(1,os.get_terminal_size(0).columns)
	y=os.get_terminal_size(0).lines
	for i in range(rn(5,35)):
		print("\033[{};{}H{}".format(y-i>-1 and y-i,x,chr(rn())))
	x=rn(1,os.get_terminal_size(0).columns)
	for i in range(rn(5,35)):
		print("\033[{};{}H{}".format(y-i>-1 and y-i,x,chr(rn())))
		print("\033[{};{}H{}".format(y-i-2>-1 and y-i-1,x+16,chr(rn())))
	x=rn(1,os.get_terminal_size(0).columns)
	for i in range(rn(5,35)):
		print("\033[{};{}H{}".format(y-i>-1 and y-i,x,chr(rn())))
		print("\033[{};{}H{}".format(y-i-1>-1 and y-i-1,x+16,chr(rn())))
	x=rn(1,os.get_terminal_size(0).columns)
	for i in range(rn(5,35)):
		y-i>-1 and print("\033[{};{}H{}".format(y-i,x,chr(rn())))
		y-i-3>-1 and print("\033[{};{}H{}".format(y-i-3,x+2,chr(rn())))
		y-i-1>-1 and print("\033[{};{}H{}".format(y-i-1,x+16,chr(rn())))
	sys.stdout.flush()
	stdscr.timeout(100)

while 1:
	if func=='d':
		draw()
	else:
		
		cmat()
	key=stdscr.getch()
	if key==27 or key==ord('q') :break
	elif key==ord('d'):func ='d'
	elif key==ord('t'):func ='t' and print("\033[0;32m")
	elif key==ord('w'):white=not white
print('\033[?1049l')
print(d_color)
curses.endwin()
