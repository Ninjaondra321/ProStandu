from selenium import webdriver
from selenium.webdriver.common.by import By


class urlGetter():
    def __init__(self, fileName):
        self.fileName = fileName
        self.driver = webdriver.Chrome()

        # Initially dispay

    def display(self):
        self.driver.get(self.getNextUrl())

        # Execute javascript code
        self.driver.execute_script("""
            
            var button = document.createElement("button");
            
            button.style = "position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1000; background-color: rgba(0, 0, 0, 0.5);";
        
        """)

    def getNextUrl(self):
        # with open(self.fileName, "r") as f:
        #     try:
        #         # Read the first line
        #         url = f.readline()
        #         # Remove the first line
        #         lines = f.readlines()
        #     except:
        #         print("No more urls")
        #         return None

        return "https://free-mp3-download.net/download.php?id=2074234767&q=UW9pZXQlMjAtJTIwZ2hvdWxGUkVOWlk="


if __name__ == "__main__":
    u = urlGetter("urls.txt")
    u.display()
