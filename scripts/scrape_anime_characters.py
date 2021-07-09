import json
from bs4 import BeautifulSoup
from requests import get
from urllib.request import urlretrieve
from time import sleep

def get_links_from_page(page_num: int):
    '''Scrapes a page of the Most Favorited characters on MyAnimeList

    Args
    -----
    page_num (int): The page number to scrape
    '''
    limit = 50 * (page_num - 1)
    url = f"https://myanimelist.net/character.php?limit={limit}"

    soup = BeautifulSoup(get(url).content, "html.parser")
    table = soup.find("table", {"class": "characters-favorites-ranking-table"})
    people = table.find_all("td", {"class": "people"})
    links = [person.find("a")["href"] for person in people]

    return links

def scrape_character(url: str):
    '''Scrapes the image and name of a specific anime character

    Args
    -----
    url (str): The URL for a specific anime character
    '''
    character_name = url.split("/")[-1].replace("_", " ")

    output_filename = f"characters/{character_name}.jpg"

    soup = BeautifulSoup(get(url).content, "html.parser")
    img_link = soup.find("table").find("a").find("img")["data-src"]

    urlretrieve(img_link, output_filename)

def main():
    pages_needed = 4

    links = []

    for page in range(pages_needed):
        links.extend(get_links_from_page(page))

    for link in links:
        scrape_character(link)
        sleep(0.5)

if __name__ == "__main__":
    main()
