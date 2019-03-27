import logging
import Utils
reload(Utils)

def checkMetering(euPic):
    meteringButton = "meteringButton.png"
    meteringData = "meteringData.png"
    hover(euPic)
    click(meteringButton)
    wait(5)
    hover(meteringData)
    logging.info("Retrieved data from Metering UI")

Utils.openWindow(Utils.addr)

Utils.loginUser(Utils.adminAcc, Utils.adminPic, Utils.password)
checkMetering(Utils.euPic)
Utils.logOutUser(Utils.adminPic)

Utils.closeWindow()