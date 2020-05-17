#!/usr/bin/python

from multiprocessing import Pool
import time
import sys
import os
import subprocess
import argparse

def main(args):
    
	parser = argparse.ArgumentParser(prog="Multiplexer", description="Aggregate Arguments and Multiprocess")

	parser.add_argument("command_file")
	parser.add_argument("-t", "--threads", help="number of threads", type=int, default="5")
	parser.add_argument("-h", "--help", help="print this help message")
	
   	command = get_command(argv[1])
   	
    test_cmd = subprocess.run(["echo wat"])
    
    with file as open(argv[2]):


if __name__ == '__main__':
	main(sys.argv)
