from selenium.common.exceptions import NoSuchElementException
from POM.Locator.LocatorInitialPage import locator

# Check for Pop-Up and Unit selection.
# We have to change the Unit selection by manually. Just give the self.ID'S
class popUp():
    def __init__(self, driver):
        self.driver = driver
        self.popupClose_css = locator.popupClose
        self.unitSelection4 = locator.unitSelection4_css
        self.unitSelection5 = locator.unitSelection5_css
        self.unitSelection6 = locator.unitSelection6_css

    def closeInitialPopUp(self):
        try:
            elem = self.driver.find_element_by_css_selector(self.popupClose_css)
            if elem.is_displayed():
                elem.click()
        except NoSuchElementException:
            print("Pop-Up not present on webpage")

    def unitPopUpCheck(self):
        self.driver.find_element_by_css_selector(self.unitSelection5).click()
        # We have to change the Unit selection by manually (for Parking, AllUnit). Just give the self.ID'S
        # (example:- self.unitSelection4 , self.unitSelection5 ,self.unitSelection6)
        # 6 is the last in row (AllUnit), 5 is the last in row(Parking)


