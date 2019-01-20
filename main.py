from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Time to wait for web page to be loaded.
TIME_FACTOR = 20

list_url = "https://www.imdb.com/list/ls064927382/?ref_=tt_rls_2"

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
    name = content.find("a").text
    year = content.find("span", class_="lister-item-year text-muted unbold").text
    runtime = content.find("span", class_="runtime").text
    genre = content.find("span", class_="genre").text
    point = content.find("span", class_="ipl-rating-star__rating").text
    print(name)
    print(year)
    print(runtime)
    print(genre.split(','))
    print(point)
    print("------------------")
