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
from Netflix import probe_filename, open_file

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

	def test_open_file (self) :
		filename = probe_filename
		f = open_file(filename)
		self.assertNotEqual(f, None)
		

	
# ----
# main
# ----

if __name__ == "__main__" :
    main()
