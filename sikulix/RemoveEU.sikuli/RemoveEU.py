import Utils
reload(Utils)

def removeEu(adminPic, euPic, euAcc):
    userPanelButton = "1552472947955.png"
    euLabel = "euLabel.png"
    searchBar = "searchBar.png"
    deleteButton = "deleteButton.png"
    deleteLogo = "1552545227439.png"
    confirmButton = "1552545301899.png"
    successLogo = "1552472809217.png"
    hover(adminPic)
    click(userPanelButton)
    wait(euLabel, 100)
    click(searchBar)
    type(euAcc)
    wait(euPic, 100)
    click(deleteButton)
    wait(deleteLogo, 100)
    click(confirmButton)
    wait(successLogo, 500)
    wait(5)

Utils.openWindow(Utils.addr)
Utils.loginUser(Utils.adminAcc, Utils.adminPic, Utils.password)
removeEu(Utils.adminPic, Utils.euPic, Utils.euAcc)
Utils.logOutUser(Utils.adminPic)
Utils.closeWindow()