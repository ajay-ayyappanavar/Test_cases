import pytest
from selenium.webdriver.common.by import By
import sys


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_title(self, driver):
        """
        Verify click and title of page
        :return: None
        """
        driver.get(r'https://www.lambdatest.com/selenium-playground')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[contains(text(),'Simple Form Demo')]").click()
        url = driver.current_url
        if “simple-form-demo” in url:
            print(" URL contains 'simple-form-demo' ")
        var = “Welcome to LambdaTest”
        driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys(var)
        driver.find_element(By.CSS_SELECTOR,"#showInput").click()
        var_out = driver.find_element(By.CSS_SELECTOR,"#message").text
        assert var == var_out, " Both the text are not matching"
        

    def test_item(self, driver):
        """
        Verify item submission
        :return: None
        """
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = driver.find_element(By.ID, "sampletodotext")
        email_text_field.send_keys(sample_text)

        driver.find_element(By.ID, "addbutton").click()

        li6 = driver.find_element(By.NAME, "li6")
        # sys.stderr.write(li6)
        # assert sample_text in li6
