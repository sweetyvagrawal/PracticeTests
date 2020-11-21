import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("initial_setup")
class TestAmazonSearch:
    LOGGER_NAME = "Log_AmazonSearch"
    def test_amazon_url(self, explicit_wait, logger):
        assert "https://www.amazon.com/" == self.driver.current_url

    def test_amazon_search(self, logger, explicit_wait):
        self.driver.refresh()
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys("Batman")
        self.driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()
        titles = self.driver.find_elements_by_xpath("//div/h2/a")
        for title in titles:
            try:
                assert "Batman" in title.text or "Bat_Man" in title.text or "Bat-Man" in title.text
            except:
                logger.exception("Batman text not found in title: " + title.text)

    def test_categories(self, logger):
        #self.driver.find_elements_by_xpath("//div[@class='nav-search-scope nav-sprite']")
        select = Select(self.driver.find_element_by_id('searchDropdownBox'))
        length = len(select.options)
        logger.info("total count of catogeries: " + str(length))
        options = select.options
        for option in options:
            logger.info(option.text)






















