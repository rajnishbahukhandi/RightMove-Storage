from POM.Locator.LocatorInitialPage import locator
from POM.OnlineRentForm.Popup import popUp
from POM.OnlineRentForm.Rent import RentalForm
from POM.OnlineRentForm.Insurance import insuranceSelect
from POM.CredentialsFile.Variables import var
import time
import random


class locationOfRightMoveStorage():
    def __init__(self, driver):
        self.driver = driver
        self.popupCheck = popUp(driver)
        self.digit = var.LastUnitNumber
        self.rentBtn = locator.rentBtn_xpath
        self.untRentForm = RentalForm(driver)
        self.closeRentBtn = locator.closeRentBtn_css
        self.insuranceValues = insuranceSelect(driver)
        self.validation = locator.validation_id

    def testForUnitCheck(self):
        self.popupCheck.closeInitialPopUp()
        time.sleep(0.3)
        self.popupCheck.unitPopUpCheck()
        time.sleep(0.2)
        selectUnitNumber = random.randrange(1, self.digit)
        print("selectUnitNumber ---- ", selectUnitNumber)
        self.driver.find_element_by_css_selector(".size-all tr:nth-child({}".format(selectUnitNumber) + ") .select-unit-btn").click()
        rentValue = self.driver.find_element_by_xpath(self.rentBtn)
        rentText = rentValue.text
        if "RENT" == rentText:
            self.driver.implicitly_wait(0.3)
            rentValue.click()
            time.sleep(10)
            title = self.driver.title
            print(title)
            self.untRentForm.form()
            time.sleep(14)
            self.insuranceValues.insuranceNext()
            time.sleep(15)
            validationText = self.driver.find_element_by_id(self.validation).text
            print(validationText)
            if "Please select one of the merchandise!" == validationText:
                time.sleep(2)
                self.insuranceValues.insurances()
            else:
                print("---- No validation used")
        else:
            time.sleep(2)
            self.driver.find_element_by_css_selector(self.closeRentBtn).click()
            print("---- No Rent button Available")

