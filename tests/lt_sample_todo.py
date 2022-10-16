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
        driver.get(r'https://www.lambdatest.com/selenium-playground/')
        driver.find_elements(By.XPATH, "//a[contains(text(),'Drag & Drop Sliders')]").click()
        
        elem = driver.find_element(By.XPATH,"//body/div[@id='__next']/div[1]/section[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")
        ac = ActionChains(browser)
        ac.move_to_element(elem).move_by_offset(946, 349).click().perform()
        val = driver.find_element(By.ID,"rangeSuccess").text
        assert val == '95' , " Value is not equal to 95"
       
