import unittest
import HtmlTestRunner
import os
from TestCases import SearchText
from TestCases import HomePageTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText.Search)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest.HomePage)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_title='Test Report', descriptions='Acceptance Tests' )

# run test suite using HTMLTestRunner
runner.run(test_suite)


