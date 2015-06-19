#!/usr/bin/env python3

# -------------------------------
# Netflix.py
# Copyright (C) 2015
# Brandon Gottesman and Perry Feng
# -------------------------------

def open_file(filename) :
	return open(filename)

probe_filename = "/u/downing/cs/netflix/probe.txt"
probe_file = open_file(probe_filename)

def get_movie_filename(parsed_movie_id):
	length = len(parsed_movie_id)
	string = ""
	for i in range(7 - (length - 1)):
		string += '0'
	string += parsed_movie_id[0:length - 1]
	return 'mv_' + string + '.txt'
