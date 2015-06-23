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
from Netflix import netflix_print, netflix_eval, netflix_solve, netflix_calculate_RMSE

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    def test_netflix_calculate_RMSE_1(self) :
        list_1 = [1, 1, 1]
        list_2 = [2, 2, 2]
        RMSE_value = netflix_calculate_RMSE(list_1, list_2)
        self.assertEqual(RMSE_value, 1)    

    def test_netflix_print_1(self) :
        w = StringIO("")
        i = "1"
        netflix_print(w, i)
        self.assertEqual(w.getvalue(), "1\n")

    def test_netflix_eval_1(self) :
        movie_id = "1"
        user_id = "30878"
        user_prediction = netflix_eval(movie_id, user_id)
        self.assertEqual(user_prediction, 3.7)

    def test_netflix_solve_1(self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO("")
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.7\n3.7\n3.7\n")
	
# ----
# main
# ----

if __name__ == "__main__" :
    main()
