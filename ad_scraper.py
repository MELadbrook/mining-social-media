"""Use Beautiful Soup to parse Facebook data."""

import csv
from bs4 import BeautifulSoup

rows = []
with open("advertisers_you've_interacted_with.html") as page:
    soup = BeautifulSoup(page, "html.parser")
    contents = soup.find("div", class_="_4t5n")
    ad_list = contents.find_all("div", class_="uiBoxWhite")
    for item in ad_list:
        advert = item.find("div", class_="_2let").get_text()
        timeaccessed = item.find("div", class_="_2lem").get_text()
        row = {
            "advert": advert,
            "timeaccessed": timeaccessed
            }
        rows.append(row)
with open("all_advertisers.csv", "w") as csvfile:
    fieldnames = ["advert", "timeaccessed"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

