import Utils
from sikuli import *
reload(Utils)
import logging

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
    logging.info("Entered API publish UI")

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
    type("base")
    click(pathPanel)
    logging.info("Set API basic info")

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
    click("1553238264700.png")
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
    logging.info("Set API access path")

def setApiSec():
    wait(2)
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
    wait(2)
    newSecDefButton = Pattern("newSecDefButton.png").targetOffset(45,35)
    clientCheck = "clientCheck.png"
    secretCheck = "secretCheck.png"
    propButton = "propButton.png"
    click(newSecDefButton)
    wait(1)
    click(clientCheck)
    click(secretCheck)
    click(propButton)
    logging.info("Set and defined API security")

def defApiProp():
    wait(2)
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
    click(deployButton)
    logging.info("Set API properties")
    
def deployApi():
    wait(2)
    createCompButton = "createCompButton.png"
    opSwitch = "opSwitch.png"
    opSwitchLoc = Pattern("opSwitchLoc.png").targetOffset(-6,-2)
    foldUseless = "foldUseless.png"
    invoke = "invoke.png"
    invokeLoc1 = Pattern("invokeLoc1.png").targetOffset(2,-15)
    invokeLoc2 = Pattern("invokeLoc2.png").targetOffset(-10,-10)
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
    click(createCompButton)
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
    logging.info("Edited API")

def defApiQuota():
    wait(2)
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
    logging.info("Set API quota")
    openWindow("http://marketplace.9.112.244.252.nip.io/#/market/detail?prod=5c90e38d1a057d000194ccd0&enablebuy=false&isTested=false")

def testApi():
    wait(2)
    successMessage = "successMessage.png"
    testApiButton = "testApiButton.png"
    type(Key.PAGE_DOWN)
    click(testApiButton)
    wait(successMessage, 200)
    logging.info("Tested API")

def reviewApi(oaPic):
    reviewApiButton = "reviewApiButton.png"
    reviewApiDetailButton = Pattern("reviewApiDetailButton.png").targetOffset(51,2)
    passApiRadio = "passApiRadio.png"
    confirmApiButton = "confirmApiButton.png"
    hover(oaPic)
    click(reviewApiButton)
    wait(2)
    click(reviewApiDetailButton)
    wait(2)
    click(passApiRadio)
    click(confirmApiButton)
    
def purchaseApi(apiName):
    cloudMarketplaceButton = "cloudMarketplaceButton.png"
    prodSearchBar = "prodSearchBar.png"
    searchProdButton = "searchProdButton.png"
    prodButton = "prodButton.png"
    purchaseApiButton = "purchaseApiButton.png"
    confirmPurchaseApiButton = "confirmPurchaseApiButton.png"
    finishApiPurchaseButton = "finishApiPurchaseButton.png"
    click(cloudMarketplaceButton)
    click(prodSearchBar)
    type(apiName)
    wait(1)
    click(searchProdButton)
    wait(2)
    click(prodButton)
    wait(2)
    click(purchaseApiButton)
    wait(1)
    click(confirmPurchaseApiButton)
    click(finishApiPurchaseButton)
    wait("1553241878992.png", 100)

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
    Utils.closeWindow()

Utils.openWindow(Utils.addr)

Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
publishApi(Utils.euPic, Utils.apiName, Utils.testUserAcc, Utils.password)
setApiBasicInfo(Utils.yamlTitle, Utils.apiVersion)
setApiPath()
setApiSec()
defApiSec()
defApiProp()
deployApi()
defApiQuota()
testApi()
Utils.logOutUser(Utils.euPic)

Utils.loginUser(Utils.oaAcc, Utils.oaPic, Utils.password)
reviewApi(Utils.oaPic)
Utils.logOutUser(Utils.oaPic)

Utils.loginUser(Utils.cusAcc, Utils.cusPic, Utils.password)
purchaseApi(Utils.apiName)
checkApiPurchase(Utils.cusPic)
Utils.logOutUser(Utils.cusPic)

Utils.closeWindow()