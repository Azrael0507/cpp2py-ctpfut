# -*- coding: utf-8 -*-
from MyApi import *
import thosttraderapi as api


def main():
	actionlist = []
	print("start init instance")
	myapi=CTradeApi()
	myapi.start()
	input()

if __name__ == '__main__':
	main()
