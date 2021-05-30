from selenium.common.exceptions import NoSuchElementException
from POM.Locator.LocatorRentOnlineAndInsurance import rentMoveIn
from POM.TakeScreenshot.Screenshotmethod import capture
from POM.OnlineRentForm.Payment import pay
import time


class insuranceSelect():
    def __init__(self, driver):
        self.driver = driver
        self.insurancesBtn = rentMoveIn.insurances_xpath
        self.merchandiseBtn = rentMoveIn.merchandise_xpath
        self.insuranceNextBtn = rentMoveIn.insuranceNextBtn_id
        self.paymentOnlineMethod = pay(driver)

    def insurances(self):
        try:
            insurancesCheck = self.driver.find_element_by_xpath(self.insurancesBtn)
            if insurancesCheck.is_displayed():
                insurancesCheck.click()
                self.driver.implicitly_wait(0.3)
                self.merchandise()
                time.sleep(0.3)
                self.insuranceNext()
                time.sleep(15)
                capture.captureScreen()
                # self.paymentOnlineMethod.paymentOnline()
        except NoSuchElementException:
            print("No insurances on the page.")
            self.driver.implicitly_wait(0.3)
            self.merchandise()
            time.sleep(0.3)
            self.insuranceNext()
            time.sleep(15)
            capture.captureScreen()
            # self.paymentOnlineMethod.paymentOnline()

    def merchandise(self):
        self.driver.find_element_by_xpath(self.merchandiseBtn).click()

    def insuranceNext(self):
        self.driver.find_element_by_id(self.insuranceNextBtn).click()