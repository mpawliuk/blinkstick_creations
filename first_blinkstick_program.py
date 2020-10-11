# https://arvydas.github.io/blinkstick-python/
from blinkstick import blinkstick
import time
import random

def p(n):
	"""Pause the system briefly. This is used to make light shows."""
	time.sleep(n/4)

def off(device):
	""" Turn off all lights."""
	for i in range(8):
		device.set_color(index=i, red=0, green=0, blue=0)

bstick = blinkstick.find_first()

# Fixed data on the blinkstick
print(bstick.get_serial())
print(bstick.get_manufacturer())
print(bstick.get_description())

# Changeable data stored on the blinkstick
print(bstick.get_info_block1())
print(bstick.get_info_block2())


# The gradient effects
for i in range(5):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	for i in range(8):
		bstick.set_color(index=i, red=int(r*i//8), green=int(g*i//8), blue=int(b*i//8))
		p(1)
	off(bstick)
	
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	for i in range(8):
		bstick.set_color(index=7-i, red=int(r*i//8), green=int(g*i//8), blue=int(b*i//8))
		p(1)
	off(bstick)