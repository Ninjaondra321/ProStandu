# 0. IMPORTS
import requests
import json

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def search(s):
    r = requests.get("https://free-mp3-download.net/search.php?s=" + s)

    if r.status_code != 200:
        raise Exception("Failed to load page")

    # Parse r.text to json
    # Return json

    x = json.loads(r.text)

    for item in x["data"]:
        print(item)

    print(x)

    return x


class StandaTheDJ():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.song_stack = []

    def search(self, text):
        self.driver.get("https://free-mp3-download.net/")

        text = text.replace("'", "")

        search_bar = self.driver.find_element(By.ID, "q")

        search_bar.send_keys(text)

        search_button = self.driver.find_element(By.ID, "snd")
        search_button.click()

        # Wait for results

        results = self.driver.find_element(By.ID, "results")
        self.driver.implicitly_wait(500)

        table = results.find_element(By.ID, "results_t")
        link = table.find_element(By.TAG_NAME, "a")

        print(link.get_attribute("href"))

        # Open on new tab
        self.driver.execute_script("window.open('" +
                                   link.get_attribute("href") + "', '_blank');")

        self.driver.execute_script(f"""
            let link = document.getElementsByClassName("white-text text-white);
            link.href = {self.get_next_song()}
        """)

    def get_next_song(self):
        if len(self.song_stack) == 0:
            return None
        return self.song_stack.pop()

    def close(self):
        self.driver.close()


if __name__ == "__main__":

    l = [
        "Apashe - I'm A Dragon - VIP",
        "Apashe - Lacrimosa",
        # "Apashe - Lord & Master",
        # "RIOT - Buck Shots",
        # "Evilwave - Pray for Us",
        # "Qoiet - ghoulFRENZY",
        # "UNSECRET - No Mercy"
    ]

    s = StandaTheDJ()

    for song in l:
        s.search(song)

    input("Press enter to exit")
    s.close()
