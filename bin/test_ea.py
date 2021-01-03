"""Test ea file
"""
from ea import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-1-3"

def test():
	"""Tests the ea function in the ea class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert ea.ea() == "ea", "test failed"
	#assert ea.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
