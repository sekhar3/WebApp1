from selenium import webdriver


class WebDriverClass:

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome(r"..\..\Driver\chromedriver.exe")
        elif browserName == "safari":
            driver = webdriver.Safari()
        elif browserName == "firefox":
            driver = webdriver.Firefox(
                executable_path=r"..\..\Driver\\Driver\geckodriver.exe")

        return driver
