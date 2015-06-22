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
from Netflix import netflix_eval, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    def test_netflix_eval(self) :
        movie_id = 1
        user_id = 30878
        user_prediction = netflix_eval(movie_id, user_id)
        self.assertEqual(user_prediction, 3.7)

    def test_netflix_solve(self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO("")
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.7\n3.7\n3.7\n")
	
# ----
# main
# ----

if __name__ == "__main__" :
    main()
