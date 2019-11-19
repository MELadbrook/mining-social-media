"""Script for scraping wikipedia sites."""

import csv
import time
from bs4 import BeautifulSoup
import requests

rows = []


urls = ["https://en.wikipedia.org/wiki/Category:Women_computer_scientists",
        "https://en.wikipedia.org/w/index.php?title=Category:Women_computer"
        "_scientists &pagefrom=Lin%2C+Ming+C.%0AMing+C.+Lin#mw-pages"]


def scrape_content(url):
    time.sleep(2)
    page = requests.get(url)
    page_content = page.content

    soup = BeautifulSoup(page_content, "html.parser")
    content = soup.find("div", class_="mw-category")
    all_groupings = content.find_all("div", class_="mw-category-group")
    for grouping in all_groupings:
        names_list = grouping.find("ul")
        category = grouping.find("h3").get_text()
        alphabetical_names = names_list.find_all("li")

        for alphabetical_name in alphabetical_names:
            name = alphabetical_name.text
            anchortag = alphabetical_name.find("a", href = True)
            link = anchortag["href"]
            letter_name = category

            row = {"name": name.encode("utf-8"),
                   "link": link.encode("utf-8"),
                   "letter_name": letter_name.encode("utf-8")}
            rows.append(row)


for url in urls:
    scrape_content(url)

with open("names.csv", "w") as csvfile:
    fieldnames = ["name", "link", "letter_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

