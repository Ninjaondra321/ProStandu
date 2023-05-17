import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class urlGetter():
    def __init__(self, fileName):
        self.fileName = fileName
        self.driver = webdriver.Chrome()
        self.keepChecking = True

        # Initially dispay
        self.display()

    def display(self):
        self.driver.get(self.getNextUrl())
        nextUrl = self.getNextUrl()
        # Execute javascript code
        self.driver.execute_script("""
            var button = document.createElement("button");
            
            button.innerHTML = "Next song";
            button.onclick = function() {
                window.location.href = " """ + nextUrl + """ ";
                };

            button.style = "position: fixed; top: 0; left: 0; width:100vw; height:100px; z-index: 1000; background-color: rgba(230, 230, 230, 0.5); ";
            console.log(button);
            document.body.appendChild(button);
            
        """)

        print("done")

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

    def close(self):
        self.driver.close()

    def startChecking(self):
        self.keepChecking = True
        # while self.keepChecking:


if __name__ == "__main__":
    u = urlGetter("urls.txt")
    u.display()
