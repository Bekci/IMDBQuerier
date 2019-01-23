"""
Represents the film objects in the list.
"""

class Film(object):
    def __init__(self, f_name, f_year, f_rating, f_genres,
                    f_runtime, f_storyline, f_type):

        self.name = f_name
        self.year = f_year
        self.rating = f_rating
        self.genres = f_rating
        self.runtime = f_runtime
        self.storyline = f_storyline
        self.fim_type = f_type
