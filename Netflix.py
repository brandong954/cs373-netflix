# Copyright (C) 2015
# Brandon Gottesman & Perry Feng
# ---------------------------

# ------------
# imports
# ------------

import json
import code
from urllib.request import urlopen
from math import sqrt
#from numpy import mean, sqrt, square, subtract

# ------------
# Load Caches from URLs
# ------------

# Average Movie Rating Cache URL
amrc_URL = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json")
average_movie_rating_cache = json.loads(amrc_URL.read().decode(amrc_URL.info().get_param('charset') or 'utf-8'))

# Average Viewer Rating Cache URL
avrc_URL = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json")
average_viewer_rating_cache = json.loads(avrc_URL.read().decode(avrc_URL.info().get_param('charset') or 'utf-8'))

# Probe Answers Cache URL
pac_URL = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json")
probe_answers_cache = json.loads(pac_URL.read().decode(pac_URL.info().get_param('charset') or 'utf-8')) 


# ------------
# netflix_calculate_RMSE
# ------------
def netflix_calculate_RMSE (a, p) :
    """
    O(1) in space
    O(n) in time
    a is list 1
    b is list 2 
    returns RMSE calculated using the two lists
    """
    assert len(a) > 0
    assert len(a) == len(p)
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)
    x = sqrt(v / len(a))
    return x


# ------------
# netflix_eval
# ------------

def netflix_eval (movie_id, user_id) :
    """
    movie_id is a string
    user_id is a string
    returns a prediction of the user's rating
    """
    assert type(movie_id) is str
    assert type(user_id) is str
    x = average_movie_rating_cache[movie_id]
    y = average_viewer_rating_cache[user_id]
    assert x > 0
    assert y > 0
    z = round((0.91 * (x + y) - 2.88), 1)
    return 1.0 if (z < 1.0) else 5.0 if (z > 5.0) else z

# -------------
# netflix_print
# -------------

def netflix_print (w, i) :
    """
    w a writer
    i either the movie_id or prediction
    writes out the prediction to w
    """
    assert hasattr(w, "write")
    w.write(str(i) + "\n")


# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    produces a prediction result
    """

    assert hasattr(r, "read")
    assert hasattr(w, "write")

    # list of actual rating
    answer_list = []

    # list of our generated predictions
    prediction_list = []

    movie_id = None
    for s in r :
        if ':' in s :
            movie_id = s[:-2]
            netflix_print(w, movie_id + ":")
        else :
            user_id = s[:-1]
            user_prediction = netflix_eval(movie_id, user_id) 
            answer_list += [probe_answers_cache[movie_id][user_id]]
            prediction_list += [user_prediction]
            netflix_print(w, user_prediction)

    print("RMSE: " + str(round(netflix_calculate_RMSE(answer_list, prediction_list), 2)))     


