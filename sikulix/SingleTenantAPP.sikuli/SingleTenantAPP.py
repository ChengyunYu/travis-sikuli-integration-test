import Utils
reload(Utils)

import Utils
reload(Utils)

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
    tenantSelect = "tenantSelect.png"
    singleTenantOption = "singleTenantOption.png"
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
    click(tenantSelect)
    click(singleTenantOption)
    wait(1)
    click(nextStepButtonInter)
    
def assembleApp():
    defaultClass = "defaultClass.png"
    frontendImage = "frontendImage.png"
    frontendImageLoc = Pattern("frontendImageLoc.png").targetOffset(-456,7)
    foldDefault = "foldDefault.png"
    storagePanel = "storagePanel.png"
    localClass = "localClass.png"
    cephfs = "cephfs.png"
    cephfsLoc = Pattern("cephfsLoc.png").targetOffset(-17,22)
    foldLocal = "foldLocal.png"
    helmPanel = "helmPanel.png"
    localCharts = "localCharts.png"
    redis = "redis.png"
    redisLoc = "redisLoc.png"
    wait(defaultClass, 100)
    click(defaultClass)
    wait(1)
    drag(frontendImage)
    hover(frontendImageLoc)
    wait(2)
    dropAt(frontendImageLoc)
    wait(1)
    click(foldDefault)
    wait(1)
    click(storagePanel)
    wait(1)
    click(localClass)
    wait(1)
    drag(cephfs)
    hover(cephfsLoc)
    wait(2)
    dropAt(cephfsLoc)
    wait(1)
    click(foldLocal)
    wait(1)
    click(helmPanel)
    wait(1)
    click(localCharts)
    wait(1)
    drag(redis)
    hover(redisLoc)
    wait(2)
    dropAt(redisLoc)
    wait(1)
    click("1553336411713.png")
    wait(1)
    click(Pattern("1553337312264.png").targetOffset(57,0))
    wait(1)
    click("1553337212510.png")
    wait(1)
    click(Pattern("1553337221006.png").targetOffset(53,1))
    wait(1)
    click("1553337437188.png")
    wait(1)
    click("1553337459889.png")
    wait(1)
    Utils.tripleClick("1553337492447.png")
    type(Key.BACKSPACE + "frauto")
    click(Pattern("1553337531750.png").targetOffset(-55,1))
    wait(1)
    click("1553338459141.png")
    wait(1)
    click("1553338487956.png")
    wait(1)
    click(Pattern("1553338515812.png").targetOffset(43,-3))
    wait(1)
    click("1553338548450.png")
    wait(1)
    click("1553338571677.png")
    type("GET_HOSTS_FROM")
    wait(1)
    click("1553338612638.png")
    type("env")
    wait(1)
    click(Pattern("1553338641055.png").targetOffset(212,-4))
    wait(1)
    click("1553337825209.png")
    wait(1)
    click(Pattern("1553337886766.png").targetOffset(-16,12))
    wait(1)
    click("1553337932805.png")
    wait(1)
    click("1553337843687.png")
    wait(1)
    click(Pattern("1553337967737.png").targetOffset(170,-2))
    click(Pattern("1553650888239.png").targetOffset(45,-87))
    wait(1)
    click("1553338124034.png")
    wait(1)
    click("1553338153331.png")
    click("1553338170330.png")
    wait(1)
    Utils.tripleClick(Pattern("1553651226189.png").targetOffset(-119,28))
    type(Key.BACKSPACE + "REDIS_MASTER_SERVICE_HOST")
    wait(1)
    click(Pattern("1553338248463.png").targetOffset(-75,0))
    wait(1)
    click(Pattern("1553338272935.png").targetOffset(222,1))
    wait(2)
    click(Pattern("1553654644016.png").targetOffset(579,5))
    wait(1)
    click("1553338153331.png")
    click("1553338170330.png")
    wait(1)
    Utils.tripleClick(Pattern("1553651438974.png").targetOffset(-102,30))
    type(Key.BACKSPACE + "REDIS_SLAVE_SERVICE_HOST")
    wait(1)
    click(Pattern("1553338248463.png").targetOffset(-75,0))
    wait(1)
    click(Pattern("1553338385729.png").targetOffset(228,2))
    wait(1)
    
def deployTestApp():
    successMessage = "successMessage.png"
    closeSuccessMessage = Pattern("closeSuccessMessage.png").targetOffset(139,-39)
    testAppAddr = "testAppAddr.png"
    confirmButton = "confirmButton.png"
    finalStep = "finalStep.png"
    addAppPlan = "addAppPlan.png"
    appPlanNameInput = "appPlanNameInput.png"
    confirmAppPlan = "confirmAppPlan.png"
    testDeployButton = "1552562215493.png"
    click(testDeployButton)
    wait(successMessage, 1000)
    hover(successMessage)
    click(closeSuccessMessage)
    wait(2)
    click(finalStep)
    wait(2)
    click(addAppPlan)
    wait(1)
    click(appPlanNameInput)
    type("Prod")
    wait(1)
    click(confirmAppPlan)
    wait(1)
    click(finalStep)
    wait(2)
    click(testAppAddr)
    checkAppFrontend()
    click(confirmButton)

def applyAppProd():
    deployAppName = "deployAppName.png"
    deployAppDesc = Pattern("deployAppDesc.png").targetOffset(-313,-4)
    confirmDeployButton = "confirmDeployButton.png"
    wait(2)
    applyProdButton = "applyProdButton.png"
    click(applyProdButton)
    wait(1)
    click(deployAppName)
    type(prodName)
    click(deployAppDesc)
    type(prodName)
    click(confirmDeployButton)
    if exists("1553244778458.png"):
        click("1553244788332.png")

def approveProdApp():
    notButton = "notButton.png"
    newNoti = Pattern("newNoti.png").targetOffset(-94,4)
    appPanel = "appPanel.png"
    reviewAppButton = "reviewAppButton.png"
    agreeRadio = "agreeRadio.png"
    submitReviewButton = "submitReviewButton.png"
    hover(notButton)
    click(newNoti)
    wait(1)
    click(appPanel)
    wait(1)
    click(reviewAppButton)
    wait(2)
    click(agreeRadio)
    click(submitReviewButton)
    wait(5)

def purchaseApp(appName):
    wait(1)
    cloudMarketplaceButton = Pattern("cloudMarketplaceButton.png").targetOffset(-280,1)
    prodSearchBar = "prodSearchBar.png"
    searchProdButton = "searchProdButton.png"
    prodAppButton = "prodAppButton.png"
    appPlan = "appPlan.png"
    purchaseAppButton = "purchaseAppButton.png"
    confirmPurchaseApiButton = "confirmPurchaseApiButton.png"
    finishApiPurchaseButton = Pattern("finishApiPurchaseButton.png").targetOffset(-15,5)
    click(cloudMarketplaceButton)
    click(prodSearchBar)
    type(appName)
    click(searchProdButton)
    wait(2)
    click(prodAppButton)
    wait(2)
    click(appPlan)
    wait(2)
    click(purchaseAppButton)
    wait(1)
    click(confirmPurchaseApiButton)
    wait(1)
    click(finishApiPurchaseButton)
    wait(1)
    Utils.closeWindow()

def deployAppOrder(euPic):
    notButton = "notButton.png"
    orderNot = Pattern("orderNot.png").targetOffset(-106,0)
    orderAccPic = "orderAccPic.png"
    deployOrderButton = "deployOrderButton.png"
    successProd = Pattern("1553244842178.png").targetOffset(144,-41)
    hover(euPic)
    hover(notButton)
    wait(1)
    click(orderNot)
    wait(2)
    hover(orderAccPic)
    wait(1)
    click(deployOrderButton)
    wait(successProd, 500)
    click(successProd)

def visitApp():
    purchasedAppButton = Pattern("purchasedAppButton.png").targetOffset(0,38)
    appTitlePic = Pattern("appTitlePic.png").targetOffset(-144,24)
    hover(cusPic)
    click(purchasedAppButton)
    wait(2)
    click(appTitlePic)
    wait(appFrontend, 50)
    hover(appFrontend)
    Utils.closeWindow()
    
appName = "autoregs"
prodName = "autoapps"
frontendAddr = "http://9.112.249.90/frontend-autotestorg-prod/"

Utils.openWindow(Utils.addr)
Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
publishApp(Utils.euPic, appName, appName, Utils.testUserAcc, Utils.password)
assembleApp()
deployTestApp()
applyAppProd()
Utils.logOutUser(Utils.euPic)

Utils.loginUser(Utils.oaAcc, Utils.oaPic, Utils.password)
approveProdApp()
Utils.logOutUser(Utils.oaPic)

Utils.loginUser(Utils.cusAcc, Utils.cusPic, Utils.password)
purchaseApp(appName)
Utils.logOutUser(Utils.cusPic)

Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
deployAppOrder(Utils.euPic)
Utils.logOutUser(Utils.euPic)

Utils.loginUser(Utils.cusAcc, Utils.cusPic, Utils.password)
visitApp(Utils.cusPic)
Utils.logOutUser(Utils.cusPic)

Utils.closeWindow()