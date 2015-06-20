#!/usr/bin/env python3

# -------------------------------
# TestNetflix.py
# Copyright (C) 2015
# Brandon Gottesman and Perry Feng
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
from Netflix import probe_filename, open_file, get_movie_filename

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

	def test_open_file (self) :
		filename = probe_filename
		f = open_file(filename)
		self.assertNotEqual(f, None)
		
	def test_get_movie_filename(self) :
		movie_filename = get_movie_filename('1:')
		self.assertEqual(movie_filename, 'mv_0000001.txt')
				
	def test_get_movie_rating_list(self) :
		average
				
	
# ----
# main
# ----

if __name__ == "__main__" :
    main()
