class locator():

    # Check the popup and the validation message.
    popupClose = ".featherlight-close-icon"
    rentBtn_xpath = "(//a[contains(text(),'Rent')])[5]"
    closeRentBtn_css = ".featherlight-close-icon"
    validation_id = "validation_message_5_71"

    # all units for different locations.
    # sometimes the all unit in the 4th, 5th and 6th position.
    # So in that case we just add the position manually on the script.
    unitSelection4_css = ".tab-link:nth-child(4) > span:nth-child(1)"
    unitSelection5_css = ".tab-link:nth-child(5) > span:nth-child(1)"
    unitSelection6_css = ".tab-link:nth-child(6) > span:nth-child(1)"