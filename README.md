# RightMove-Storage

Right Move Storage is an experienced storage management company focused on providing effective operational services for properties throughout the United States. 
Understand the challenges of today’s complex real estate market and how it impacts the storage industry. Team has a proven track record of maximizing asset performance and profitability, resulting in improved NOI and asset valuation for our clients.

Right Move Storage having the United States different locations, each location having different storage unit prices.
The storage unit including are Small, Medium, Large, X-Large, Parking, All Units.
The user will choose any unit and click on the “Select” button. After that will fill in the information and choose the insurance and done the payment.
The selection of the unit will go on the “Lease” and “Parking Lease” Agreement. Where the user can check info and signature on it.


POM (Page Object Module) Contains:-

 Locator - It having all the webElements. 

 OnlineRentalForm - It having the calling method for the Rent, Pop-Up, Insurance, Payment.

 Module - It is the center of the project, all the methods calling here.

 CredentialsFile - It having the credential. The user can edit. 

 TakeScreenshot- It haveing a method for the screenshot. And the current system time will display on the screenshot.

 TestCases - It having the unittest.TestCase class for run the test cases.


User control :-

 -> User can control variables.py (Credentials) for Email_Id, Current_Url, LastUnitNumber (for Select range button).

 -> User can control Popup.py (OnlineRentalForm) for change the function id of unitPopUpCheck method.
 We have to change the Unit selection by manually (for Parking, AllUnit). Just give the self.ID'S
 (example:- self.unitSelection4 , self.unitSelection5 ,self.unitSelection6)
 6 is the last in row (AllUnit), 5 is the last in row(Parking)


Need to install :- 

 The Python Package Index (PyPI) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by     the Python community.

 https://pypi.org/


1. The selenium package is used to automate web browser interaction from Python. Supported Python Versions Python 2.7, 3.4+

  pip3 install selenium

2. The main idea is to simplify management of binary drivers for different browsers. For install the ChromeDriverManager

   from webdriver_manager.chrome import ChromeDriverManager

   pip3 install webdriver-manager


3. Faker is a Python package that generates fake data for you.

   from faker import Faker

   pip3 install Faker


4. Use for random values of integer.

   Import random


5. Current time use on screenshot.

   from datetime import datetime

   now = datetime.now()

   current_time = now.strftime("%H:%M:%S")


6. PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard. Used for taking screenshot.

   pip3 install PyAutoGUI




