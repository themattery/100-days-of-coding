# Web Scraping the 100 top movies from Empire
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# TODO 0: Get empire's webpage html code
response = requests.get(URL)
empire_webpage = response.text

# TODO 1: Create the soup
soup = BeautifulSoup(empire_webpage, 'html.parser')

# TODO 2: Get a list with all the movies
all_movies = soup.find_all(name='h3', class_='title')

# TODO 3: Reverse the order of the list
all_movies.reverse()

# TODO 4: Save the list into a new file
with open("movies.txt", "a", encoding="utf-8") as file:
    for movie in all_movies:
        file.write(f"{movie.text}\n")
