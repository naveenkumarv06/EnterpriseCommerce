from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import TimeOut
from Utilities.EventLog import Log


class BasePage(Log):


    def __init__(self, driver):
        self.driver = driver


    def do_click(self, web_element):
        # log = self.get_ogger()
        # log.info("Clicking on element {}".format(web_element)[1])
        WebDriverWait(self.driver, TimeOut.fast).until(EC.visibility_of_element_located(web_element)).click()


    def do_send_keys(self, web_element, text):
        # log = self.get_ogger()
        # log.info(" Entering Text to the element {}".format(web_element[1]))
        WebDriverWait(self.driver, TimeOut.fast).until(EC.visibility_of_element_located(web_element)).send_keys(text)

    def get_element_text(self, web_element):
        # log = self.get_ogger()
        # log.info("Getting the Text from element {}".format(web_element[1]))
        element = WebDriverWait(self.driver, TimeOut.fast).until(EC.visibility_of_element_located(web_element))
        return element.text

    def get_title(self, text):
        # log = self.get_ogger()
        # log.info("Getting the page Title")
        WebDriverWait(self.driver, TimeOut.avg).until(EC.title_is(text))
        return self.driver.title

    def is_enabled(self, web_element):
        element = WebDriverWait(self.driver, TimeOut.fast).until(EC.visibility_of_element_located(web_element))
        return bool(element)

    def select_dropdown(self, web_element, text):
        WebDriverWait(self.driver,TimeOut.fast).until(EC.visibility_of_element_located(web_element))
        element = self.driver.find_elements(web_element)
        for el in element:
            print(el)
            if el.text == text:
                el.click()
                break

    def select_dropdown_by_select_class(self, web_element, text):
        element = WebDriverWait(self.driver, TimeOut.fast).until(EC.visibility_of_element_located(web_element))
        select = Select(element)
        value_list = select.options
        for ele in value_list:
            if ele.text == text:
                ele.click()
                break