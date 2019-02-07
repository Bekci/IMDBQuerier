from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from film_content_parser import obtain_film_object
from parser_config import check_film_object
from html_creator import create_html_file

# Time to wait for web page to be loaded.
TIME_FACTOR = 3

# Give the URL of the imdb list.
list_url = "https://www.imdb.com/list/ls047677021/?ref_=tt_rels_1"

print("Opening a webdriver")
driver = webdriver.Chrome()

# driver.maximize_window()
driver.get(list_url)

print("Waiting the website to be loaded")
# Wait browser to load the page.
time.sleep(TIME_FACTOR)

content = driver.page_source.encode('utf-16').strip()
soup = BeautifulSoup(content, 'lxml')

# Obtain all films
film_contents = soup.find_all("div", class_="lister-item mode-detail")

wanted_films = []

list_header = soup.find("h1", class_='header list-name').text

print("Parsing and querying films")
for all_content in film_contents:
    img_source = all_content.find('div', class_='lister-item-image ribbonize').find('img')
    content = all_content.find('div', class_='lister-item-content')
    current_film = obtain_film_object(content, img_source)
    if check_film_object(current_film):
        wanted_films.append(current_film)

create_html_file(wanted_films, list_header)
print("New html created with the name ",list_header )

driver.close()
