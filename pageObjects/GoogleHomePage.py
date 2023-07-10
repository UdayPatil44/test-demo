import time

from selenium.webdriver.common.by import By
from Utilities.customLogger import logGen


class GoogleSearch:
    textbox_search = "//textarea[@id='APjFqb']"

    def __init__(self, driver):
        self.driver = driver

    def testGooglesearch(self):
        logger = logGen.loggen()

        # searching the search box field.
        search_input = self.driver.find_element(By.XPATH, self.textbox_search)
        # Entering the text into search box.
        search_input.send_keys('Cute cats')
        time.sleep(2)
        # Pressing ENTER button to initiate search
        search_input.submit()
        time.sleep(3)
        # Locator of the desired element
        search_results = self.driver.find_elements(By.XPATH,
                                                   "//h3[@class='LC20lb MBeuO DKV0Md']")  # //div//cite[@role='text']
        search_list = []
        for i in search_results:
            search_list.append(i.text)

        #logger.info(search_list)

        third_element = search_list[4]
        expected_value = "750+ Cute Cat Pictures | Download Free Images on ..."

        logger.info("Third Result is :%s", third_element)
        assert third_element == expected_value, "Third element does not match the expected value."
