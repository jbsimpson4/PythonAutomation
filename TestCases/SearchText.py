####Webdriver Properties###
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchText(unittest.TestCase):
     @classmethod     
     def setUpClass(inst):
        # create a new Chrome session
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://www.google.com/")
        inst.driver.title     

     def test_search_by_text(self):
       # get the search textbox
       self.search_field = self.driver.find_element_by_name("q")
       
       # enter search keyword and submit
       self.search_field.send_keys("Selenium WebDriver Interview questions")
       self.search_field.submit

       # get the list of elements which are displayed after the search
       # currently on result page using find_elements_by_class_name method

       lists = self.driver.find_elements_by_class_name("r")
       
       self.assertEqual(11, len(lists))

     def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.send_keys("Python class")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, len(list_new))
  
     @classmethod
     def tearDownClass(inst):
         # close the browser window
         inst.driver.quit()

# command line execution
#if __name__ == '__main__':
 #  unittest.main() 
       

