# https://arvydas.github.io/blinkstick-python/
from blinkstick import blinkstick
import time

def p(n):
	"""Pause the system briefly. This is used to make light shows."""
	time.sleep(n/4)

def off(device):
	""" Turn off all lights."""
	for i in range(8):
		device.set_color(index=i, red=0, green=0, blue=0)

def bi(device):
	""" Turn on bi colours.
	(214,2,112), (155,79,150), and (0,56,168)
	"""
	for i in range(0,3):
		device.set_color(index=i, red=214, green=2, blue=112)
	for i in range(3,5):
		device.set_color(index=i, red=155, green=79, blue=150)
	for i in range(5,8):
		device.set_color(index=i, red=0, green=56, blue=168)

def rainbow(device):
	""" Turn on rainbow colours.
	HEX: #ff0000 RGB: (255, 0, 0), 
	HEX: #ffa500 RGB: (255, 165, 0), 
	HEX: #ffff00 RGB: (255, 255, 0), 
	HEX: #008000 RGB: (0, 128, 0), 
	HEX: #0000ff RGB: (0, 0, 255), 
	HEX: #4b0082 RGB: (75, 0, 130), 
	HEX: #ee82ee RGB: (238, 130, 238).
	"""
	device.set_color(index=0, red=255, green=0, blue=0)
	device.set_color(index=1, red=255, green=165, blue=0)
	device.set_color(index=2, red=255, green=255, blue=0)
	device.set_color(index=3, red=0, green=128, blue=0)
	device.set_color(index=4, red=0, green=0, blue=255)
	device.set_color(index=5, red=75, green=0, blue=130)
	device.set_color(index=6, red=75, green=2, blue=130)
	device.set_color(index=7, red=238, green=130, blue=238)

def beat(device, time, colour, lights):
	r,g,b = colour[:3]
	for i in lights:
		device.set_color(index=i, red=r, green=g, blue=b)
	p(time)
	off(device)
	p(time)

def beat_full(device, time, colour1, colour2, index1, index2):
	r,g,b = colour1[:3]
	r2,g2,b2 = colour2[:3]
	device.set_color(index=index1, red=r, green=g, blue=b)
	device.set_color(index=index2, red=r2, green=g2, blue=b2)
	p(time)
	off(device)
	p(time)

def flush(device,time=1):
	for i in range(8):
		beat(device, time, (0,0,255), range(i))
		beat(device, time, (0,0,255), range(i,9))
	for i in range(8,0,-1):
		beat(device, time, (0,0,255), range(i))
		beat(device, time, (0,0,255), range(i,9))

def x(device, colour, time=1):
	for i in range(3):
		beat(bstick, time, colour, [i, 7-i])
	for i in range(3,0,-1):
		beat(bstick, time, colour, [i, 7-i])

def pairs(device, colour, time=1):
	for i in range(5):
		beat(bstick, time, colour, [i, i+2])
	for i in range(5,0,-1):
		beat(bstick, time, colour, [i, i+2])

def pairs_full(device, colour1, colour2, time=1):
	for i in range(5):
		beat_full(bstick, time, colour1, colour2, i, i+2)
	for i in range(5,0,-1):
		beat_full(bstick, time, colour1, colour2, i, i+2)

def trips(device, colour1, time=1):
	for i in range(3):
		beat(bstick, time, colour1, [i, i+2,i+4])
	for i in range(3,0,-1):
		beat(bstick, time, colour1, [i, i+2,i+4])

def quads(device, colour1, time=1):
	for i in range(2):
		beat(bstick, time, colour1, [i, i+2,i+4,i+6])

bstick = blinkstick.find_first()
bstick.set_max_rgb_value(50)


def routine1(device,c, c2, r):
	for _ in range(r):
		x(device, c, t)
	for _ in range(r):
		x(device, c2, t)
	for _ in range(r):
		pairs(device,c,t)
	for _ in range(r):
		pairs(device,c2,t)
	for _ in range(r):
		pairs_full(device,c,c2,t)
	for _ in range(r+1):
		trips(device,c,t)
	for _ in range(r+1):
		trips(device,c2,t)
	for _ in range(r+2):
		quads(device,c,t)
	for _ in range(r+2):
		quads(device,c2,t)
	for _ in range(r+3):
		bi(device)
		p(t)
		off(device)
		p(t)

	rainbow(device)
	p(5)

	off(device)

t = 0.6
c = (214,2,112)
c2 = (0,0,255)
r = 2
routine1(bstick,c,c2,r)
