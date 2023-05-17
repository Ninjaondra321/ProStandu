import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class urlGetter():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://free-mp3-download.net/")

    def getUrl(self, text):

        # Edit the string, becuase the website doesn't accept apostrophes
        text = text.replace("'", "")

        search_bar = self.driver.find_element(By.ID, "q")

        # Clear search bar and type the song name
        search_bar.clear()
        search_bar.send_keys(text)

        search_button = self.driver.find_element(By.ID, "snd")
        search_button.click()

        # Jinak to exploduje!!
        # TODO: Klidně podle rychlosti wifi
        time.sleep(2)

        results = self.driver.find_element(By.ID, "results")
        table = results.find_element(By.ID, "results_t")
        a = table.find_element(By.TAG_NAME, "a")
        link = a.get_attribute("href")

        print(self.driver)
        print(len(self.driver.window_handles))

        # Save the url to a file
        with open("urls.txt", "a") as f:
            f.write(link + "\n")

        print(link)
        return link

    def close(self):
        self.driver.close()


if __name__ == "__main__":

    l = [
        "Apashe - I'm A Dragon - VIP",
        "Apashe - Lacrimosa",
        "Apashe - Lord & Master",
        "RIOT - Buck Shots",
        "Evilwave - Pray for Us",
        "Qoiet - ghoulFRENZY",
        "UNSECRET - No Mercy"
    ]

    s = urlGetter()

    for song in l:
        s.getUrl(song)
        input("Press enter to continue")

    input("Press enter to exit")
    s.close()
