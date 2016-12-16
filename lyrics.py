import requests
from bs4 import BeautifulSoup

number_of_pages = 4
band_name = "Selena Gomez"
url_name = band_name.lower().replace(" ", "-")

with open("{}_lyrics.txt", "w") as outfile:
    for counter in range(1, number_of_pages +1):
        url = "http://www.metrolyrics.com/{}-alpage-{}.html".format(url_name, counter)

        content = requests.get(url).text
        souper = BeautifulSoup(content, "html.parser")
        results = souper.find_all("a", class_='title ')
        for result in results:
            alt = result.attrs["alt"]
            if band_name in alt:
                lyric_url= result.attrs['href']
                content = requests.get(lyric_url).text
                souper = BeautifulSoup(content, "html.parser")
                results = souper.find(id="lyrics-body-text")
                outfile.write(results.text)
