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

    # -----------
    # tests for netflix_calculate_RMSE()
    # -----------

    def test_netflix_calculate_RMSE_1(self) :
        list_1 = [1, 1, 1]
        list_2 = [2, 2, 2]
        RMSE_value = netflix_calculate_RMSE(list_1, list_2)
        self.assertEqual(RMSE_value, 1)    

    def test_netflix_calculate_RMSE_2(self) :
        list_1 = [0, 0, 0]
        list_2 = [0, 0, 0]
        RMSE_value = netflix_calculate_RMSE(list_1, list_2)
        self.assertEqual(RMSE_value, 0)    
        
    def test_netflix_calculate_RMSE_3(self) :
        list_1 = [1999]
        list_2 = [2455]
        RMSE_value = netflix_calculate_RMSE(list_1, list_2)
        self.assertEqual(RMSE_value, 456)    
        
    # -----------
    # tests for netflix_print()
    # -----------

    def test_netflix_print_1(self) :
        w = StringIO("")
        i = "1"
        netflix_print(w, i)
        self.assertEqual(w.getvalue(), "1\n")

    def test_netflix_print_2(self) :
        w = StringIO("")
        i = ""
        netflix_print(w, i)
        self.assertEqual(w.getvalue(), "\n")

    def test_netflix_print_3(self) :
        w = StringIO("")
        i = "-1"
        netflix_print(w, i)
        self.assertEqual(w.getvalue(), "-1\n")

    # -----------
    # tests for netflix_eval()
    # -----------

    def test_netflix_eval_1(self) :
        movie_id = "1"
        user_id = "30878"
        user_prediction = netflix_eval(movie_id, user_id)
        self.assertEqual(user_prediction, 3.7)

    # -----------
    # tests for netflix_solve()
    # -----------

    def test_netflix_solve_1(self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO("")
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.7\n3.5\n3.6\n")
	
# ----
# main
# ----

if __name__ == "__main__" :
    main()
