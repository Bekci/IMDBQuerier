"""
Parse strings obtained from the html to get the film metadata.
Fix metadata and create an film object to be use it later.
"""

from ClassFilm import Film

"""
Eliminate parenthesis from the text.
'(2019)' -> '2019'
"""
def parse_film_year(year_text):
    return year_text.replace('(' , '').replace(')' , '')


"""
Obtain decimal value of the score from its text.
'7'  -> 70
'7,9'-> 79
"""
def parse_imdb_score(score_text):
    units_digit = 0
    if ',' in score_text:
        tens_digit, units_digit = score_text.split(',')
    else:
        tens_digit = score_text.split(',')[0]
    return int(tens_digit) * 10 + int(units_digit)


"""
Parse runtime in minutes from runtime text.
"134 min" -> 134
"""
def parse_runtime(runtime_text):
    return runtime_text.split(' ')[0]


"""
From the string of genres, obtain the genres list.
Remove extra spaces and new line characters.
Return genres in a list.
"""
def obtain_all_genres(genres_text):
    obtained_genres = []
    for genre in genres_text.split(','):
        obtained_genres.append(genre.replace('\n', '').replace(' ', ''))
    return obtained_genres


"""
Storyline obtained as text from the html yet some characters must be deleted
from it.
"""
def obtain_story_line(story_text):
    return story_text.replace('\n', '')

"""
Determine the film type from the year text.
A TV-series will include '-' but a film will not include.
"""
def determine_film_type(year_text):
    if '–' in year_text:
        return 'tv-series'
    return 'film'

"""
Take a html block representing the film item
Apply parsing and return film object
"""
def obtain_film_object(content):
    # Runtime and score of a film might not given in the list item.
    runtime = "unknown"
    point = "unknown"

    raw_name = content.find("a").text
    raw_year = content.find("span", class_="lister-item-year text-muted unbold").text
    raw_runtime = content.find("span", class_="runtime")

    if raw_runtime is not None:
        raw_runtime = raw_runtime.text
        runtime = int(parse_runtime(raw_runtime))

    raw_genre = content.find("span", class_="genre").text
    raw_point = content.find("span", class_="ipl-rating-star__rating")

    if raw_point is not None:
        raw_point = raw_point.text
        point = int(parse_imdb_score(raw_point))

    raw_storyline = content.find("p", class_="").text

    year = parse_film_year(raw_year)
    genre_list = obtain_all_genres(raw_genre)
    storyline = obtain_story_line(raw_storyline)
    f_type = determine_film_type(year)

    return Film(raw_name, raw_year, point, genre_list, runtime, storyline, f_type)
