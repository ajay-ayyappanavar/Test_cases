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
        driver.implicitly_wait(10)
        driver.find_elements(By.XPATH, "//a[contains(text(),'Drag & Drop Sliders')]").click()
        
        elem = driver.find_element(By.XPATH,"//body/div[@id='__next']/div[1]/section[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")
        ac = ActionChains(browser)
        ac.move_to_element(elem).move_by_offset(946, 349).click().perform()
        val = driver.find_element(By.ID,"rangeSuccess").text
        assert val == '95' , " Value is not equal to 95"
    
    def test_validation(self, driver):
        
        driver.get(r'https://www.lambdatest.com/selenium-playground')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//a[contains(text(),'Input Form Submit')]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//button[contains(text(),'Submit')]').click()
        name = driver.find_element(By.XPATH, '//input[@id='name']')
        verify = "Please fill in the fileds"
        msg = name.getattr(name,"validationMessage")
        assert verify == msg, " validation message is not as ecpected"
        name.send_keys('Shiva')
        driver.find_element(By.CSS_SELECTOR,'#inputEmail4').send_keys('shiva@email.com')
        driver.find_element(By.CSS_SELECTOR,'#inputPassword4').send_keys('shiva@1234')
        driver.find_element(By.XPATH,'//input[@id='company']').send_keys('xyz')
        driver.find_element(By.XPATH,'//input[@id='websitename']').send_keys('abs')
        select = driver.find_element(By.XPATH, '//body/div[@id='__next']/div[1]/section[3]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/select[1]').click()
        select.select_by_visible_text('United States')
        driver.find_element(By.CSS_SELECTOR,'#inputCity').send_keys('chik')
        driver.find_element(By.CSS_SELECTOR,'#inputAddress1').send_keys('anything')
        driver.find_element(By.CSS_SELECTOR,'#inputAddress2').send_keys('allgod')
        driver.find_element(By.XPATH,'//input[@id='inputState']').send_keys('KA')
        driver.find_element(By.CSS_SELECTOR,'#inputZip').send_keys('675435')
        driver.find_element(By.XPATH, '//button[contains(text(),'Submit')]').click()
        
        final_msg = 'Thanks for contacting us, we will get back to you '
        equal = driver.find_element(By.XPATH,"//p[contains(text(),'Thanks for contacting us, we will get back to you ')]").text
        assert final_msg == equal, "Message is not as expected"
