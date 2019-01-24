

def start_html():
    return """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Selected Films</title>
      </head>
      <body>
        <ul>
    """

def close_html():
    return """
        </ul>
      </body>
    </html>
    """

def create_table_from_object(film_object):
    return """
                <li>
                  <table>
                    <tr>
                      <td rowspan="5">%s</td>
                      <td colspan="3"> %s</td>
                    </tr>
                    <tr>
                      <td> %s mins</td>
                      <td>%s </td>
                      <td>%s </td>
                    </tr>
                    <tr>
                      <td colspan="3">%s</td>
                    </tr>
                  </table>
                </li>
    """ % (film_object.get_image_html(), film_object.get_title(), film_object.runtime,
            film_object.get_genres_string(), film_object.rating, film_object.storyline)

def create_html_file(film_objects_list):
    film_html_str = ""
    for film_object in film_objects_list:
        film_html_str += create_table_from_object(film_object)
    html_file = open("temp.html", "w")
    html_file.write(start_html() + film_html_str + close_html() )
