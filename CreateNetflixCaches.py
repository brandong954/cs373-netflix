#!/usr/bin/env python3

# -------------------------------
# Netflix.py
# Copyright (C) 2015
# Brandon Gottesman and Perry Feng
# -------------------------------

movies_directory = "/u/downing/cs/netflix/training_set/"

# def get_movie_filename(parsed_movie_id):
# 	length = len(parsed_movie_id)
# 	string = ""
# 	for i in range(7 - (length - 1)):
# 		string += '0'
# 	string += parsed_movie_id[0:length - 1]
# 	return 'mv_' + string + '.txt'

def create_caches() :
	#limit = 17770
	limit = 1
	for i in range(1, limit + 1) :
		zeros_string = ""
		movie_file_path = str(i)
		length = len(movie_file_path)
		for j in range(7 - (length)) :
			zeros_string += '0'
		movie_file_path = movies_directory + 'mv_' + zeros_string + movie_file_path + '.txt'
		movie_file = open(movie_file_path)
		for s in movie_file :
			print(s, end = "")	
			
# ----
# main
# ----

if __name__ == "__main__" :
    create_caches()
