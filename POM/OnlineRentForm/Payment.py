from POM.Locator.LocatorPayment import payMethod


class pay():
    def __init__(self, driver):
        self.driver = driver
        self.nameOnCard = payMethod.nameOnCard_id
        self.cardNumber = payMethod.cardNumber_id
        self.cardType = payMethod.cardType_id
        self.cvv = payMethod.cvv_id
        self.expDateMMYY = payMethod.expDateMMYY_id
        self.paymentNxtBtn = payMethod.paymentNxtBtn_id

    def paymentOnline(self):
        self.driver.find_element_by_id(self.nameOnCard).send_keys("Ray Rajnish")
        self.driver.find_element_by_id(self.cardNumber).send_keys("4242424242424242")
        self.driver.find_element_by_id(self.cardType).click()
        self.driver.find_element_by_id(self.cvv).send_keys("123")
        self.driver.find_element_by_id(self.expDateMMYY).send_keys("12/23")
        self.driver.find_element_by_id(self.paymentNxtBtn).click()
