# Copyright (C) 2015
# Brandon Gottesman & Perry Feng
# ---------------------------

# ------------
# imports
# ------------

import json
import code
from math import sqrt
#from numpy import mean, sqrt, square, subtract

average_movie_rating_cache = None
average_user_rating_cache = None
probe_answers = None

with open('./Average_Movie_Rating_Cache.json') as data_file:    
    average_movie_rating_cache = json.load(data_file)

with open('./ezo55-Average_Viewer_Rating_Cache.json') as data_file:    
    average_user_rating_cache = json.load(data_file)

with open('./pam2599-probe_solutions.json') as data_file:
    probe_answers = json.load(data_file)

# ------------
# netflix_calculate_RMSE
# ------------
def netflix_calculate_RMSE (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)
    return sqrt(v / len(a))

# ------------
# netflix_eval
# ------------

def netflix_eval (movie_id, user_id) :
    """
    returns a prediction of the user's rating
    """
    x = average_movie_rating_cache[movie_id]
    y = average_user_rating_cache[user_id]
    # z = round((x+y)/2, 1)
    z = 0.940 * (x + y) - 2.870
    return 1.0 if (z < 1.0) else 5.0 if (z > 5.0) else z
    # return z if (z >= 1.0 and z <= 5.0) else 1.0 if (z < 1.0) else 5.0

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
    answer_list = []
    prediction_list = []
    # code.interact(local=locals())


    movie_id = None
    for s in r :
        if ':' in s :
            movie_id = s[:-2]
            netflix_print(w, movie_id + ":")
        else :
            user_id = s[:-1]
            user_prediction = netflix_eval(movie_id, user_id) 
            answer_list += [probe_answers[movie_id][user_id]]
            prediction_list += [user_prediction]
            netflix_print(w, user_prediction)

    print("RMSE: " + str(netflix_calculate_RMSE(answer_list, prediction_list)))     


