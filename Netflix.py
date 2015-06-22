# Copyright (C) 2015
# Brandon Gottesman & Perry Feng
# ---------------------------

# ------------
# imports
# ------------

from json import load
from numpy import mean, sqrt, square, subtract

average_movie_rating_cache = None
average_user_rating_cache = None


# ------------
# netflix_calculate_RMSE
# ------------
def netflix_calculate_RMSE (list1, list2) :
    """
    calculates RMSE from two lists
    list1 is first list
    list2 is second list
    returns RMSE
    """
    return sqrt(mean(square(subtract(list1, list2))))

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    """
    """

# ------------
# netflix_eval
# ------------

def netflix_eval (movie_id, user_id) :
    """
    """
    return 1   

# -------------
# netflix_print
# -------------

def netflix_print (w, i) :
    """
    w a writer
    i either the movie_id or prediction
    """
    w.write(str(i) + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    print("loading caches")
    with open('./Average_Movie_Rating_Cache.json') as data_file:    
        average_movie_rating_cache = load(data_file)
    # with open('./Average_User_Rating_Cache.json') as data_file:    
        # average_user_rating_cache = load(data_file)
    
    print("done loading caches")

    movie_id = None
    for s in r :
        if ':' in s:
            movie_id = s[0:len(s)-1]
            netflix_print(w, s)
        else:
            user_id = s
            user_prediction = netflix_eval(movie_id, user_id) 
            netflix_print(w, user_prediction)



