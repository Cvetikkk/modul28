import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browserChrome():
    _web_driver = webdriver.Chrome()
    yield _web_driver
    _web_driver.quit()

@pytest.fixture(scope="session")
def browserFirefox():
    _web_driver = webdriver.Firefox()
    yield _web_driver
    _web_driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
