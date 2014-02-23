from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://vancouver.ca')
        self.browser.get('http://vancouver.ca/your-government/work-for-the-city-of-vancouver.aspx')
        self.browser.get('http://vancouver.ca/your-government/find-and-apply-for-a-job.aspx')
        self.browser.get('https://vanfep.city.vancouver.bc.ca/sap/bc/webdynpro/sap/hrrcf_a_posting_apply?PARAM=cG9zdF9pbnN0X2d1aWQ9NTJGMERCNTk2MDEwMDBEOUUxMDA4MDAwQUMxQTAxMTImY2FuZF90eXBlPUVYVA%3d%3d&sap-client=453&sap-language=EN')

        # She notices the page title and header mention to-do lists
        self.assertIn('Vancouver', self.browser.title) 
        self.fail('Finish the test!') 

        # She is invited to enter a to-do item straight aways

if __name__ == '__main__':  
    unittest.main()
