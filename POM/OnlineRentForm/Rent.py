from POM.Locator.LocatorRentOnlineAndInsurance import rentMoveIn
from selenium.webdriver.support.ui import Select
from POM.CredentialsFile.Variables import var
import time
import random

# Used faker library for the fake information.
from faker import Faker
fake = Faker('en_US')
firstName = fake.first_name()
lastName = fake.last_name()
address = fake.address()
city = fake.city_suffix()
aptUnitNumber = fake.street_address()
zipcode = fake.postalcode()
emergencyContactEmail = fake.safe_email()
emergencyContactFirstname = fake.name_female()
phone = random.randint(9912345690, 9912345699)
SSN = random.randint(4005, 4050)
emergencyContactPhone = random.randint(8888345670, 8888345688)
militaryPhone = random.randint(7778345670, 7778345679)
driverLicense = random.randint(494045901, 494045909)


class RentalForm():
    def __init__(self, driver):
        self.driver = driver
        self.firstName = rentMoveIn.firstName_id
        self.lastName = rentMoveIn.lastName_id
        self.email = rentMoveIn.email_id
        self.cellPhone = rentMoveIn.cellPhone_id
        self.homePhone = rentMoveIn.homePhone_id
        self.streetAddress = rentMoveIn.streetAddress_id
        self.apt_unitnumber = rentMoveIn.apt_unitnumber_id
        self.city = rentMoveIn.city_id
        self.state = rentMoveIn.state_id
        self.stateSelect = rentMoveIn.stateSelectValue
        self.zipcode = rentMoveIn.zipcode_id
        self.dateOfBirth = rentMoveIn.dateOfBirth_id
        self.driverLicense = rentMoveIn.driverLicense_id
        self.SSN = rentMoveIn.SSN_id
        self.driverLicenseState = rentMoveIn.driverLicenseState_id
        self.selectDriverLicenseState = rentMoveIn.selectDriverLicenseStateValue
        self.emergencyContactFirstName = rentMoveIn.emergencyContactFirstName_id
        self.emergencyContactLastName = rentMoveIn.emergencyContactLastName_id
        self.emergencyContactEmail = rentMoveIn.emergencyContactEmail_id
        self.emergencyContactPhone = rentMoveIn.emergencyContactPhone_id
        self.miscellaneousCheckBox = rentMoveIn.miscellaneousCheckBox_id
        self.militaryBase = rentMoveIn.militaryBase_id
        self.militaryContact = rentMoveIn.militaryContact_id
        self.militaryPhone = rentMoveIn.militaryPhone_id
        self.businessCheckbox = rentMoveIn.businessCheckbox_id
        self.password = rentMoveIn.password_id
        self.passwordConfirmation = rentMoveIn.passwordConfirmation_id
        self.nextButton = rentMoveIn.nextButton_id
        self.userEmailId = var.Email_id
        self.validationError = rentMoveIn.validationError_xpath

    # Used faker library for the fake information.
    def form(self):
        self.driver.find_element_by_id(self.firstName).send_keys(firstName)
        self.driver.find_element_by_id(self.lastName).send_keys(lastName)
        self.driver.find_element_by_id(self.email).send_keys(self.userEmailId)
        self.driver.find_element_by_id(self.cellPhone).send_keys("989898989809")
        self.driver.find_element_by_id(self.homePhone).send_keys(phone)
        self.driver.find_element_by_id(self.streetAddress).send_keys(address)
        self.driver.find_element_by_id(self.apt_unitnumber).send_keys(aptUnitNumber)
        self.driver.find_element_by_id(self.city).send_keys("Denver")
        select_state = Select(self.driver.find_element_by_id(self.state))
        select_state.select_by_index(self.stateSelect)
        self.driver.find_element_by_id(self.zipcode).send_keys(zipcode)
        self.driver.find_element_by_id(self.dateOfBirth).send_keys("04/03/1993")
        self.driver.find_element_by_id(self.driverLicense).send_keys(driverLicense)
        selectValue_DriverLicenseState = Select(self.driver.find_element_by_id(self.driverLicenseState))
        selectValue_DriverLicenseState.select_by_index(self.selectDriverLicenseState)
        time.sleep(0.2)
        self.driver.find_element_by_id(self.emergencyContactFirstName).send_keys(emergencyContactFirstname)
        self.driver.find_element_by_id(self.emergencyContactLastName).send_keys(lastName)
        self.driver.find_element_by_id(self.emergencyContactEmail).send_keys(emergencyContactEmail)
        self.driver.find_element_by_id(self.emergencyContactPhone).send_keys(emergencyContactPhone)
        self.driver.find_element_by_id(self.miscellaneousCheckBox).click()
        self.driver.find_element_by_id(self.militaryBase).send_keys("US military")
        self.driver.find_element_by_id(self.militaryContact).send_keys("test military")
        self.driver.find_element_by_id(self.militaryPhone).send_keys(militaryPhone)
        self.driver.find_element_by_id(self.businessCheckbox).click()
        self.driver.find_element_by_id(self.password).send_keys("1234")
        self.driver.find_element_by_id(self.passwordConfirmation).send_keys("1234")
        self.driver.find_element_by_id(self.nextButton).click()
        time.sleep(6)
        self.validationSSN()

    def validationSSN(self):
        validationErrorText = self.driver.find_element_by_xpath(self.validationError).text
        print(validationErrorText)
        if "There was a problem with your submission. Errors have been highlighted below." == validationErrorText:
            self.driver.find_element_by_id(self.SSN).send_keys(SSN)
            time.sleep(0.1)
            self.driver.find_element_by_id(self.nextButton).click()
        else:
            print("Validation error not matched.")