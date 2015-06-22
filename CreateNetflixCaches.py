#!/usr/bin/env python3

# -------------------------------
# Netflix.py
# Copyright (C) 2015
# Brandon Gottesman and Perry Feng
# -------------------------------

from json import dump

movies_directory = "/u/downing/cs/netflix/training_set/"

def get_movie_file(movie_id) :
	zeros_string = ""
	movie_file_path = str(movie_id)
	length = len(movie_file_path)
	for j in range(7 - (length)) :
		zeros_string += '0'
	movie_file_path = movies_directory + 'mv_' + zeros_string + movie_file_path + '.txt'
	movie_file = open(movie_file_path)
	return movie_file

def get_movie_rating_average(movie_file) :
	movie_file.readline()
	movie_rating_list = []
	for movie_line in movie_file:
		rating = int(movie_line[movie_line.index(',') + 1])
		movie_rating_list += [rating]
	return sum(movie_rating_list) / len(movie_rating_list)	

def create_caches() :
	movie_id_limit = 17770
	movie_average_dic = {}
	for i in range(1, movie_id_limit + 1) :
		movie_file = get_movie_file(i)
		movie_rating_average = get_movie_rating_average(movie_file)
		movie_average_dic[i] = movie_rating_average			
	with open("Average_Movie_Rating_Cache.json", "w+") as outfile:
    		dump(movie_average_dic, outfile, indent=4)
# ----
# main
# ----

if __name__ == "__main__" :
    create_caches()
