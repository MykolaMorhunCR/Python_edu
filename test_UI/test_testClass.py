from selenium import webdriver
import unittest
import time
class BasePage:

    def __init__(self, webDriver):
        self.driver = webDriver

class SearchResultsPage(BasePage):

    def verifyTitle(self, query):
        assert query in self.driver.title

    def printResults(self):
        resultList = self.driver.find_elements_by_xpath("//div/a/h3")

        print(resultList)

        for element in resultList:
            print(element.text)

        assert len(resultList) > 0

class GoooglePage(BasePage):

    def openPage(self):
        self.driver.get('http://www.google.com/')

        return self

    def searchQuery(self, query):
        searchField = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        searchField.clear()
        searchField.send_keys(query)
        searchField.submit()

        assert query in self.driver.title

        return SearchResultsPage(self.driver)

    # def printResults(self):
    #     time.sleep(5)
    #     resultList = self.driver.find_elements_by_xpath("//div/a/h3")
    #
    #     print(resultList)
    #
    #     for element in resultList:
    #         print(element.text)

class UITestClass(unittest.TestCase):

    def test_searchTitleTest(self):
        driver = webdriver.Chrome(r'C:\Users\Call\Downloads\chromedriver.exe')

        GoooglePage(driver)\
            .openPage()\
            .searchQuery("music")\
            .verifyTitle("music")

    def test_searchResultTest(self):
        driver = webdriver.Chrome(r'C:\Users\Call\Downloads\chromedriver.exe')

        GoooglePage(driver)\
            .openPage()\
            .searchQuery("facebook")\
            .printResults()





