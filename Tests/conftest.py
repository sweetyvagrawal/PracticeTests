import logging
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def initial_setup(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="class")
def explicit_wait(request) -> WebDriverWait:
    return WebDriverWait(request.cls.driver, 10)


@pytest.fixture(scope="class")
def action_chains(request) -> ActionChains:
    return ActionChains(request.cls.driver)


@pytest.fixture(scope="class")
def logger(request):
    logger_name = request.cls.LOGGER_NAME
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler(str(Path(__file__).parent.parent) + "\\Logs\\" + logger_name + ".log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
