from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from film_content_parser import obtain_film_object
from parser_config import check_film_object

# Time to wait for web page to be loaded.
TIME_FACTOR = 20

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
film_contents = soup.find_all("div", class_="lister-item-content")

for content in film_contents:
    current_film = obtain_film_object(content)
    check_film_object(current_film)
