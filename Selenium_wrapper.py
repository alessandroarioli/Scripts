from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui



def EmailValidator(numbers, file_out):
    with open(numbers, 'r') as lines:
        for line in lines:
            driver = webdriver.Firefox()
            driver.get("https://www.twilio.com/lookup")
            wait = ui.WebDriverWait(driver, 1)
            # assert "verifyemailaddress.io" in driver.title
            wait.until(lambda driver: driver.find_elements_by_xpath('//input[@class="demo__phone-number"]'))
            elem = driver.find_element_by_xpath('//input[@class="demo__phone-number"]')
            elem.send_keys(Keys.COMMAND + 'a')
            elem.send_keys(Keys.DELETE)
            elem.send_keys(line)
            # elem.send_keys(Keys.RETURN)
            driver.implicitly_wait(6)
            response_fake = driver.find_element_by_xpath('//div[@class="column-1-2 demo__response"]')
            response = driver.find_element_by_xpath('//div[@class="row"][2]')
            with open(file_out, 'a') as file:
                file.write(line + response.text + '\n')
                file.close()
            driver.close()

EmailValidator('./email_test.ldj', './emails_out.ldj')