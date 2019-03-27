import Utils
reload(Utils)

def addEU(adminPic, euPic, euAcc, euDN):
    userPanelButton = "1552472947955.png"
    addEUButton = "addEUButton.png"
    searchBar = "1552473438288.png"
    addButton = "1552473683952.png"
    submitButton = "1552473812817.png"
    successLogo = "1552472809217.png"
    hover(adminPic)
    click(userPanelButton)
    click(addEUButton)
    click(searchBar)
    type(euAcc)
    wait(euDN, 100)
    click(addButton)
    click(submitButton)
    wait(successLogo, 100)
    wait(5)

def initRealName(euPic, orgName):
    realNameButton = "1552477685569.png"
    realNameLabel = "realNameLabel.png"
    nameLabel = "nameLabel.png"
    nameInput = "nameInptu.png"
    nicknameLabel = "nicknameLabel.png"
    nicknameInput = "nicknameInput.png"
    addPicLabel =  "addPicLabel.png"
    picLabel = "picLabel.png"
    uploadButton = "1552478075360.png"
    preview = "1552478129993.png"
    submitButton = "submitButton.png"
    successLogo = "1552472809217-1.png"
    wait(euPic, 100)
    hover(euPic)
    click(realNameButton)
    wait(realNameLabel, 100).hover(realNameLabel)
    click(nameInput)
    type(orgName)
    click(nicknameInput)
    type(orgName)
    click(addPicLabel)
    wait(picLabel, 100)
    click(picLabel)
    click(uploadButton)
    wait(preview, 100)
    click(submitButton)
    wait(successLogo, 100)
    wait(5)

def assignOA(adminPic, oaPic, oaAcc, oaDN, orgName):
    userPanelButton = "1552472947955-1.png"
    userLabel = "userLogo.png"
    sidebarToggle = "sidebarToggle.png"
    oaButton = "OAButton.png"
    addOaButton = "addOAButton.png"
    searchBar = "searchBar.png"
    editButton = "editButton.png"
    editLabel = "1552479456083.png"    
    addOrgButton = "1552479482853.png"
    orgSearchBar = "1552480475900.png"
    assignButton = "1552479563217.png"
    submitbutton = "1552479611376.png"
    confirmButton = "1552479645306.png"
    successLogo = "1552472809217-2.png"
    hover(oaPic)
    wait(userLabel, 100).hover(userLabel)
    click(userPanelButton)
    if not exists(oaButton):
        click(sidebarToggle)
    click(oaButton)
    wait(addOaButton, 100)
    click(searchBar)
    type(oaAcc)
    wait(oaDN, 100)
    click(editButton)
    wait(editLabel, 100)
    click(addOrgButton)
    click(orgSearchBar)
    type(orgName + Key.ENTER)
    click(assignButton)
    click(submitbutton)
    click(confirmButton)
    wait(successLogo, 100)
    wait(5)

def authRealName(oaPic, euAcc):
    realNameButton = "1552472947955-2.png"
    realNameLabel = "1552481470141.png"
    searchBar = "1552473438288-1.png"
    authButton = "1552481600080.png"
    agreeRadio = "agreeRadio.png"
    submitButton = "1552479645306-1.png"
    successLogo = "1552472809217-3.png"
    hover(oaPic)
    click(realNameButton)
    wait(realNameLabel, 100)
    wait(authButton, 100).click(authButton)
    wait(agreeRadio, 100).click(agreeRadio)
    wait(2)
    type(Key.PAGE_DOWN)
    click(submitButton)
    wait(successLogo, 1000)
    wait(5)

def checkRealAuth(euPic):
    realNameButton = "1552477685569-1.png"
    realNameLabel = "realNameLabel-1.png"
    successLabel = "successLabel.png"
    wait(euPic, 100)
    hover(euPic)
    click(realNameButton)
    wait(realNameLabel, 100).hover(realNameLabel)
    hover(successLabel)

Utils.openWindow(Utils.addr)

Utils.loginUser(Utils.adminAcc, Utils.adminPic, Utils.password)
addEU(Utils.adminPic, Utils.euPic, Utils.euAcc, Utils.euDN)
Utils.logOutUser(Utils.adminPic)

Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
initRealName(Utils.euPic, Utils.orgName)
Utils.logOutUser(Utils.euPic)

Utils.loginUser(Utils.adminAcc, Utils.adminPic, Utils.password)
assignOA(Utils.adminPic, Utils.oaPic, Utils.oaAcc, Utils.oaDN, Utils.orgName)
Utils.logOutUser(Utils.adminPic)

Utils.loginUser(Utils.oaAcc, Utils.oaPic, Utils.password)
authRealName(Utils.oaPic, Utils.euAcc)
Utils.logOutUser(Utils.oaPic)

Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
checkRealAuth(Utils.euPic)
Utils.logOutUser(euPic)

Utils.closeWindow()