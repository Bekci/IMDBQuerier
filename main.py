from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from film_content_parser import obtain_film_object
from parser_config import check_film_object
from html_creator import create_html_file

# Time to wait for web page to be loaded.
TIME_FACTOR = 15

list_url = "https://www.imdb.com/list/ls069592298/?ref_=tt_rls_4"
list_url = "https://www.imdb.com/list/ls024004591/?ref_=tt_rls_2"
driver = webdriver.Chrome()

# driver.maximize_window()
driver.get(list_url)

# Wait browser to load the page.
time.sleep(TIME_FACTOR / 3)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'lxml')

# Obtain all films
film_contents = soup.find_all("div", class_="lister-item mode-detail")

wanted_films = []


for all_content in film_contents:
    img_source = all_content.find('div', class_='lister-item-image ribbonize').find('img')
    content = all_content.find('div', class_='lister-item-content')
    current_film = obtain_film_object(content, img_source)
    if check_film_object(current_film):
        wanted_films.append(current_film)

create_html_file(wanted_films)
