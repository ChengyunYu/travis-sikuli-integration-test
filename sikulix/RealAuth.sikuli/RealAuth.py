def openWindow(addr):
    english = "1552467984904.png"
    chinese = "1552468022912.png"
    newWindow = "1552467346544.png"
    mpLogo = "mpLogo.png"
    
    openApp("Google Chrome")
    click(newWindow)
    type(addr + Key.ENTER)
    if exists(english):
        click(english)
        click(chinese)
        waitVanish(english)   

def closeWindow():
    closeRegion = "closeRegion.png"
    closeButton = "closeButton.png"
    find(closeRegion).click(closeButton)


def tripleClick(img):
    click(img)
    mouseDown(Button.LEFT)
    mouseUp(Button.LEFT)
    wait(0.01)
    mouseDown(Button.LEFT)
    mouseUp(Button.LEFT)
    
def loginUser(account, accountPic, password):
    loginRegion = Pattern("loginRegion.png").targetOffset(174,2)
    loginButton = "loginButton.png"
    emailLabel = "1552375840350.png"
    emailInput = "1552375548089.png"
    passwordLabel = "1552375967992.png"
    passwordInput = "passwordInput.png"

    logOutUser(accountPic)
    logOutUser(euPic)
    logOutUser(oaPic)
    
    wait(loginRegion)
    
    find(loginRegion).click(loginRegion)
    find(emailLabel)
    tripleClick(emailInput)
    type(Key.BACKSPACE)
    type(account)
    click(emailLabel)
    find(passwordLabel)
    tripleClick(passwordInput)
    type(Key.BACKSPACE)
    type(password)
    click(loginButton)

    wait(accountPic, 100)

def logOutUser(accountPic):
    loginRegion = Pattern("loginRegion.png").targetOffset(174,2)
    logOutButton = "logOutButton.png"
    if exists(accountPic):
        hover(accountPic)
        click(logOutButton)
        wait(loginRegion, 10)
        hover(loginRegion)
    return

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
    successLogo = "1552472809217.png"
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

def assignOA(adminPic, oaAcc, oaDN, orgName):
    userPanelButton = "1552472947955.png"
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
    successLogo = "1552472809217.png"
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
    realNameButton = "1552472947955.png"
    realNameLabel = "1552481470141.png"
    searchBar = "1552473438288.png"
    authButton = "1552481600080.png"
    agreeRadio = "agreeRadio.png"
    submitButton = "1552479645306.png"
    successLogo = "1552472809217.png"

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
    realNameButton = "1552477685569.png"
    realNameLabel = "realNameLabel.png"
    successLabel = "successLabel.png"
    
    wait(euPic, 100)
    hover(euPic)
    click(realNameButton)
    wait(realNameLabel, 100).hover(realNameLabel)
    hover(successLabel)

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

def publishApp(euPic, appName, deployName, testUserAcc, password):
    publishButton = "publishButton.png"
    bufferRegion = "1552556465539.png"
    appRegion = Pattern("1552556295585.png").targetOffset(-6,113)
    appBar = "appBar.png"
    appNameInput = "appNameInput.png"
    deployNameInput = "deployNameInput.png"
    labelSelector = "labelSelector.png"
    label = "1552557837570.png"
    passwordRegion = "passwordRegion.png"
    accRegion = "accRegion.png"
    nextStepButton = "1552558428940.png"
    nextStepButtonInter = Pattern("1552558470804.png").targetOffset(41,5)
    uploadRegion = Pattern("uploadRegion.png").targetOffset(-11,-11)
    uploadButton = "uploadButton.png"
    jsonFile = "jsonFile.png"
    uploadButton = "1552478075360.png"
    appGraph = "appGraph.png"
    testDeployButton = "1552562215493.png"
    successMessage = "1552562632722.png"
    newWindow = "1552467346544.png"
    appSignIn = Pattern("1552562778780.png").targetOffset(60,3)
    appSignInButton = Pattern("1552562850039.png").targetOffset(-52,2)
    signInSuccess = Pattern("signInSuccess.png").targetOffset(43,2)
    finalStep = "finalStep.png"
    confirmButton = "confirmButton.png"
    appAddress = "http://9.112.249.90/productpage-autotestorg-test/productpage"
    hover(euPic)
    click(publishButton)
    hover(bufferRegion)
    wait(appRegion, 100).click(appRegion)
    wait(appBar, 100)
    click(appNameInput)
    type(appName)
    click(deployNameInput)
    type(deployName)
    click(labelSelector)
    click(label)
    click(passwordRegion)
    type(password)
    click(accRegion)
    type(testUserAcc)
    click(nextStepButton)
    wait(5)
    click(nextStepButtonInter)
    wait(10)
    find(uploadRegion)
    hover(uploadRegion)
    click(uploadRegion)
    click(jsonFile)
    click(uploadButton)
    wait(appGraph, 100).hover(appGraph)
    click(testDeployButton)
    wait(successMessage, 1000)
    click(newWindow)
    type(appAddress + Key.ENTER)
    wait(5)
    click(appSignIn)
    click(appSignInButton)
    wait(signInSuccess, 20).hover(signInSuccess)
    closeWindow()
    wait(2)
    click(finalStep)
    click(confirmButton)
    
def publishApi(euPic, apiName, testUserAcc, password):
    publishButton = "publishButton.png"
    bufferRegion = "bufferRegion.png"
    apiButton = "apiButton.png"
    apiTitleInput = "apiTitleInput.png"
    apiNameInput = "apiNameInput.png"
    apiLabelSelector = "apiLabelSelector.png"
    apiLabel = "apiLabel.png"
    apiUploadPanel = "apiUploadPanel.png"
    picLabel = "picLabel.png"
    uploadButton = "uploadButton.png"
    nextStepButton = "nextStepButton.png"
    hover(euPic)
    click(publishButton)
    hover(bufferRegion)
    click(apiButton)
    wait(2)
    click(apiTitleInput)
    type(apiName)
    wait(2)
    click(apiNameInput)
    type(apiName)
    click(apiLabelSelector)
    click(apiLabel)
    click(apiUploadPanel)
    click(picLabel)
    click(uploadButton)
    click(nextStepButton)
    wait(2)

def setApiBasicInfo(yamlTitle, apiVersion):
    newYamlButton = "newYamlButton.png"
    yamlTitleInput = "yamlTitleInput.png"
    yamlNameInput = "yamlNameInput.png"
    yamlVersionInput = "yamlVersionInput.png"
    basicPathInput = "basicPathInput.png"
    pathPanel = "pathPanel.png"
    click(newYamlButton) 
    click(yamlTitleInput)
    type(yamlTitle)
    click(yamlNameInput)
    type(yamlTitle)
    click(yamlVersionInput)
    type(apiVersion)
    click(basicPathInput)
    type("tag1")
    click(pathPanel)

def setApiPath():
    newPathButton = Pattern("newPathButton.png").targetOffset(62,25)
    pathNameInput = "pathNameInput.png"
    getOpButton = "getOpButton.png"
    newResponseButton = Pattern("newResponseButton.png").targetOffset(14,51)
    responseNumberInput = "1552912480541.png"
    responseTypeSelect = "responseTypeSelect.png"
    stringOption = "1552912557249.png"
    responseDescriptionInput = "1552912593236.png"
    saveResponseButton = "1552912673823.png"
    saveOpButton = Pattern("saveOpButton.png").targetOffset(13,-203)
    savePathButton = Pattern("savePathButton.png").targetOffset(15,-24)
    foldButton = Pattern("foldButton.png").targetOffset(5,-2)
    foldPathButton = Pattern("foldPathButton.png").targetOffset(49,-12)
    secButton = "1552914523976.png"
    stringOptionDown = Pattern("stringOptionDown.png").targetOffset(-13,29)
    saveOpButton2 = Pattern("savePathButton2.png").targetOffset(44,-5)
    wait(5)
    click(newPathButton)
    click(pathNameInput)
    type("/tag1")
    click(getOpButton)
    wait(2)
    click(newResponseButton)
    type(Key.PAGE_DOWN)
    click(responseNumberInput)
    type("200")
    click(responseTypeSelect)
    click(stringOption)
    click(responseDescriptionInput)
    type("successful")
    click(saveResponseButton)
    click(saveOpButton)
    click(foldButton)
    click(savePathButton)
    click(foldPathButton)
    wait(5)
    click(newPathButton)
    click(pathNameInput)
    type("/tag2")
    click(getOpButton)
    type(Key.PAGE_DOWN)
    wait(2)
    type(Key.PAGE_DOWN)
    click(newResponseButton)
    type(Key.PAGE_DOWN)
    click(responseNumberInput)
    type("200")
    click(responseTypeSelect)
    click(stringOptionDown)
    click(responseDescriptionInput)
    type("successful")
    click(saveResponseButton)
    type(Key.PAGE_UP)
    click(saveOpButton2)
    click(foldButton)
    click(savePathButton)
    click(foldPathButton)    
    click(secButton)
    

def setApiSec():
    newSecButton = Pattern("newSecButton.png").targetOffset(47,30)
    secNameInput = "secNameInput.png"
    clientName = "client"
    secretName = "secret"
    secLocationSelect = "secLocationSelect.png"
    inQueryLabel = "inQueryLabel.png"
    secSaveButton = "secSaveButton.png"
    secFoldButton = Pattern("secFoldButton.png").targetOffset(44,3)
    secDefButton = "secDefButton.png"
    click(newSecButton)
    click(secNameInput)
    type(clientName)
    click(secLocationSelect)
    click(inQueryLabel)
    click(secSaveButton)
    wait(1)
    click(newSecButton)
    click(secNameInput)
    type(secretName)
    click(secLocationSelect)
    click(inQueryLabel)
    click(secSaveButton)
    click(secDefButton)

def defApiSec():
    newSecDefButton = Pattern("newSecDefButton.png").targetOffset(45,35)
    clientCheck = "clientCheck.png"
    secretCheck = "secretCheck.png"
    propButton = "propButton.png"
    click(newSecDefButton)
    wait(1)
    click(clientCheck)
    click(secretCheck)
    click(propButton)

def defApiProp():
    newPropButton = Pattern("newPropButton.png").targetOffset(36,29)
    propNameInput = "propNameInput.png"
    propValueInput = "propValueInput.png"
    propDescValueInput = "propDescValueInput.png"
    savePropButton = "savePropButton.png"
    foldPropBurron = Pattern("foldPropBurron.png").targetOffset(30,1)
    deployButton = "deployButton.png"
    prop1Name = "tag1-ptype1-url"
    prop2Name = "tag2-ptype1-url"
    prop1Value = "http://marketplace.9.112.232.156.nip.io/v1/product/hots?num=4&tags=000001&pType=1"
    prop2Value = "http://marketplace.9.110.179.122.nip.io/v1/product/hots?num=4&tags=000002&pType=1"
    prop1Desc = "URL of the tag 1 and ptype 1"
    prop2Desc = "URL of the tag 2 and ptype 1"
    click(newPropButton)
    click(propNameInput)
    type(prop1Name)
    click(propValueInput)
    type(prop1Value)
    click(propDescValueInput)
    type(prop1Desc)
    click(savePropButton)
    wait(1)
    click(foldPropBurron)
    wait(1)
    click(foldPropBurron)
    wait(1)
    click(newPropButton)
    click(propNameInput)
    type(prop2Name)
    click(propValueInput)
    type(prop2Value)
    click(propDescValueInput)
    type(prop2Desc)
    click(savePropButton)
    wait(1)
    click(foldPropBurron)
    wait(1)
    click(foldPropBurron)
    click(deployButton)
    
def deployApi():
    createCompButton = "createCompButton.png"
    opSwitch = "opSwitch.png"
    opSwitchLoc = "opSwitchLoc.png"
    foldUseless = "foldUseless.png"
    invoke = "invoke.png"
    invokeLoc1 = "invokeLoc1.png"
    invokeLoc2 = "invokeLoc2.png"
    opSwitchSettings = "opSwitchSettings.png"
    case0 = "case0.png"
    op1 = "op1.png"
    case1 = "case1.png"
    op2 = Pattern("op2.png").targetOffset(-38,12)
    invoke1 = "invoke1.png"
    invoke2 = "invoke2.png"
    invokeUrlInput = "invokeUrlInput.png"
    deployFinish = "deployFinish.png"
    toCombos = Pattern("toCombos.png").targetOffset(42,4)
    url1 = "$(tag1-ptype1-url)"
    url2 = "$(tag2-ptype1-url)"
    #click(createCompButton)
    dragDrop(opSwitch, opSwitchLoc)
    hover(opSwitch)
    click(foldUseless)
    wait(1)
    dragDrop(invoke, invokeLoc1)
    wait(1)
    dragDrop(invoke, invokeLoc2)
    wait(1)
    click(opSwitchSettings)
    click(case0)
    click(op1)
    wait(1)
    click(case1)
    wait(1)
    click(op2)
    click(invoke1)
    click(invokeUrlInput)
    type(url1)
    click(invoke2)
    click(invokeUrlInput)
    type(url2)
    click(deployFinish)
    click(toCombos)

def defApiQuota():
    newQuotaButton = "newQuotaButton.png"
    quotaNameInput = "quotaNameInput.png"
    quotaName = "Prod"
    maxInput = "maxInput.png"
    max = "200"
    maxRateInput = "maxRateInput.png"
    maxRate = "4"
    timeSelect = "timeSelect.png"
    minuteLabel = "minuteLabel.png"   
    toPublishButton = Pattern("toDepButton.png").targetOffset(22,19)
    submitApiButton = "submitApiButton.png"
    successRegion = Pattern("successRegion.png").targetOffset(252,0)
    click(newQuotaButton)
    wait(1)
    click(quotaNameInput)
    type(quotaName)
    click(maxInput)
    type(max)
    click(maxRateInput)
    type(maxRate)
    click(timeSelect)
    click(minuteLabel)
    click(toPublishButton)
    click(submitApiButton)
    wait(successRegion, 100)
    click(successRegion)
    openWindow("http://marketplace.9.112.244.252.nip.io/#/market/detail?prod=5c90e38d1a057d000194ccd0&enablebuy=false&isTested=false")

def testApi():
    successMessage = "successMessage.png"
    testApiButton = "testApiButton.png"
    type(Key.PAGE_DOWN)
    click(testApiButton)
    wait(successMessage, 200)

def purchaseApi():
    cloudMarketplaceButton = "cloudMarketplaceButton.png"
    prodSearchBar = "prodSearchBar.png"
    apiProdName = "testapie"
    searchProdButton = "searchProdButton.png"
    prodButton = "prodButton.png"
    purchaseApiButton = "purchaseApiButton.png"
    confirmPurchaseApiButton = "confirmPurchaseApiButton.png"
    finishApiPurchaseButton = "finishApiPurchaseButton.png"
    click(cloudMarketplaceButton)
    click(prodSearchBar)
    type(apiProdName)
    wait(1)
    click(searchProdButton)
    wait(2)
    click(prodButton)
    wait(2)
    click(purchaseApiButton)
    wait(1)
    click(confirmPurchaseApiButton)
    click(finishApiPurchaseButton)

def checkApiPurchase(cusPic): 
    purchasedButton = "purchasedButton.png"
    apiProdRow = "apiProdRow.png"
    seeApiMoreButton = "seeApiMoreButton.png"
    purchaseApiSuccess = Pattern("purchaseApiSuccess.png").targetOffset(-77,8)
    wait(1)
    hover(cusPic)
    click(purchasedButton)
    click(apiProdRow)
    click(seeApiMoreButton)
    wait(2)
    hover(purchaseApiSuccess)
    type(Key.DOWN, KeyModifier.CMD)
    testApi()
        
addr = "http://marketplace.9.112.244.252.nip.io/"
adminAcc = "cdlcloudadmin@cn.ibm.com"
adminPic = "1552467393989.png"
euAcc = "autotesteu@cn.ibm.com"
euPic = "euPic.png"
euDN = "euDN.png"
password = "passw0rd"
oaAcc = "autotestoa@cn.ibm.com"
oaPic = "1552986271289.png"
oaDN = "oaDN.png"
cusAcc = "autotestcus@cn.ibm.com"
cusPic = "cusPic.png"
orgName = "autotestorg"
appName = "testappl"
deployName = "testdepl"
apiName = "testapie"
yamlTitle = "tagtest"
apiVersion = "1.0.0"
testUserAcc = "testuser"

#openWindow()

#loginUser(adminAcc, adminPic, password)
#addEU(adminPic, euPic, euAcc, euDN)
#logOutUser(adminPic)

#loginUser(euAcc, euPic, password)
#initRealName(euPic, orgName)
#logOutUser(euPic)

#loginUser(adminAcc, adminPic, password)
#assignOA(adminPic, oaAcc, oaDN, orgName)
#logOutUser(adminPic)

#loginUser(oaAcc, oaPic, password)
#authRealName(oaPic, euAcc)
#logOutUser(oaPic)

#loginUser(euAcc, euPic, password)
#checkRealAuth(euPic)
#logOutUser(euPic)

#loginUser(euAcc, euPic, password)
#publishApp(euPic, appName, deployName, testUserAcc, password)
#logOutUser(euPic)

#loginUser(adminAcc, adminPic, password)
#removeEu(adminPic, euPic, euAcc)
#logOutUser(adminPic)

#loginUser(euAcc, euPic, password)
#publishApi(euPic, apiName, testUserAcc, password)
#setApiBasicInfo(yamlTitle, apiVersion)
#setApiPath()
#setApiSec()
#defApiSec()
#defApiProp()
#deployApi()
#defApiQuota()
#testApi()
#logOutUser(euPic)

#openWindow("http://marketplace.9.112.244.252.nip.io/")
#loginUser(cusAcc, cusPic, password)
#purchaseApi()
checkApiPurchase(cusPic)

#closeWindow()