"""
Define and check rules for a film object.
"""

# Rules for the film object
parse_options = {
    'type': 'film',
    'score_range_min': '6.9',
    'score_range_max': '10.0',
    'year_range_oldest': '2003',
    'year_range_newest': '2010',
    'wanted_genres': [],
    'unwanted_genres': ['romance', 'musical'],
    # Whether add or remove a film
    # whose genre neither in wanted_genres nor unwanted_genres list
    'add_not_unwanted_&_not_wanted': True,
    'include_watched': False
}

def check_genre(film_genre_list):
    for genre in film_genre_list:
        if genre in parse_options['unwanted_genres']:
            return False
    if parse_options['wanted_genres'] is None or len(parse_options['wanted_genres']) == 0:
        return True
    for genre in film_genre_list:
        if genre in parse_options['wanted_genres']:
            return True
    return parse_options['add_not_unwanted_&_not_wanted']


def check_score(score_range):
    min_score = float(parse_options['score_range_min']) * 10
    max_score = float(parse_options['score_range_max']) * 10
    return score_range >= min_score and score_range <= max_score


def check_year(year_range):
    min_year = parse_options['year_range_oldest']
    max_year = parse_options['year_range_newest']
    return year_range >= min_year and year_range <= max_year


def check_type(film_type):
    if  parse_options['type'] == 'both':
        return True
    elif  parse_options['type'] == film_type:
        return True
    return False


def check_film_object(film_object):
    if not check_genre(film_object.f_genres):
        return False
    if not check_score(film_object.rating)
        return False
    if not check_year(film_object.year)
        return False
    if not check_type(film_object.type)
        return False
    # All of the above rules applied for the object
    return True
