from pageObjects.GoogleHomePage import GoogleSearch


class Test_001_GoogleSearch:
    baseURL = "https://www.google.com/"

    def testgoogleserachresult(self, setup):
        #Launching the browser
        self.driver = setup
        #Fetching the URL
        self.driver.get(self.baseURL)

        self.gs = GoogleSearch(self.driver)
        #Executing the test case
        self.gs.testGooglesearch()
