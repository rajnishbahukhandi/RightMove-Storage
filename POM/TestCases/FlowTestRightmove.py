from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from POM.Module.MovetoLease.commonForAllLocations import locationOfRightMoveStorage
from POM.CredentialsFile.Variables import var
import unittest
import time


class FineViewRightMoveLA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        # Zoom out by 100%
        cls.driver.execute_script('document.body.style.MozTransform = "scale(0.0)";')
        cls.driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')

    def testCaseForLocations(self):
        driver = self.driver
        driver.get(var.Current_URL)
        time.sleep(2)
        rightMove = locationOfRightMoveStorage(driver)
        rightMove.testForUnitCheck()

    @classmethod
    def tearDownClass(cls):
        print("----- Pass")