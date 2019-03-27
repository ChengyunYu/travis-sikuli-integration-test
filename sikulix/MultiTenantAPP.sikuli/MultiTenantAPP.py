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

def deployTestApp():
    uploadRegion = Pattern("uploadRegion.png").targetOffset(-11,-11)
    uploadButton = "uploadButton.png"
    jsonFile = "jsonFile.png"
    jsonFile_ha = "jsonFile_ha.png"
    uploadButton = "1552478075360.png"
    appGraph = "appGraph.png"
    testDeployButton = "1552562215493.png"
    successMessage = "successMessage.png"
    closeSuccessMessage = Pattern("closeSuccessMessage.png").targetOffset(139,-39)
    testAppAddr = "testAppAddr.png"
    confirmButton = "confirmButton.png"
    finalStep = "finalStep.png"
    wait(10)
    find(uploadRegion)
    hover(uploadRegion)
    click(uploadRegion)
    click(jsonFile_ha)
    click(uploadButton)
    wait(appGraph, 100).hover(appGraph)
    click(testDeployButton)
    wait(successMessage, 1000)
    hover(successMessage)
    click(closeSuccessMessage)
    wait(2)
    click(finalStep)
    wait(2)
    click(testAppAddr)
    checkAppFrontend()
    click(confirmButton)
    wait(1)

def checkAppFrontend():
    appFrontend = "appFrontend.png"
    wait(appFrontend, 50)
    hover(appFrontend)
    Utils.closeWindow()

def deployProdApp(prodName):
    deployProdAppButton = "deployProdAppButton.png"
    deployAppName = "deployAppName.png"
    deployAppDesc = "deployAppDesc.png"
    confirmDeployButton = "confirmDeployButton.png"
    successProd = Pattern("1553244842178.png").targetOffset(144,-41)
    closeDepWindow = "closeDepWindow.png"
    applyProdButton = Pattern("applyProdButton.png").targetOffset(121,5)
    wait(1)
    click(deployProdAppButton)
    wait(1)
    click(deployAppName)
    type(prodName)
    click(deployAppDesc)
    type(prodName)
    click(confirmDeployButton)
    if exists("1553244778458.png"):
        click("1553244788332.png")
    wait(successProd, 500)
    click(successProd)
    click(closeDepWindow)
    click(applyProdButton)

def approveProdApp():
    notButton = "notButton.png"
    newNoti = Pattern("newNoti.png").targetOffset(-94,4)
    appPanel = "appPanel.png"
    reviewAppButton = "reviewAppButton.png"
    agreeRadio = "agreeRadio.png"
    submitReviewButton = "submitReviewButton.png"
    approveSuccess = "1553668914537.png"
    hover(notButton)
    click(newNoti)
    wait(1)
    click(appPanel)
    wait(1)
    click(reviewAppButton)
    wait(2)
    click(agreeRadio)
    click(submitReviewButton)
    wait(approveSuccess, 100)
    wait(5)

def purchaseApp(appName):
    cloudMarketplaceButton = "cloudMarketplaceButton.png"
    prodSearchBar = "prodSearchBar.png"
    searchProdButton = "searchProdButton.png"
    prodAppButton = "prodAppButton.png"
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
    click(purchaseAppButton)
    wait(1)
    click(confirmPurchaseApiButton)
    click(finishApiPurchaseButton)

def sendAppMessages(cusPic):
    purchasedAppButton = Pattern("purchasedAppButton.png").targetOffset(0,38)
    appTitlePic = Pattern("appTitlePic.png").targetOffset(-144,24)
    appFrontend = "appFrontend.png"
    sendButton = "sendButton.png"
    bufferC = "1553329277261.png"
    hover(cusPic)
    click(purchasedAppButton)
    wait(2)
    click(appTitlePic)
    wait(appFrontend, 50)
    click(appFrontend)
    type("hi")
    click(sendButton)
    click(bufferC)
    click(appFrontend)
    type("hello")
    click(sendButton)
    click(bufferC)
    click(appFrontend)
    type("aloha")
    click(sendButton)
    click(bufferC)
    Utils.closeWindow()
    
def accessApp(frontendAddr): 
    sshAddr = "chrome-extension://pnhechapfaindjhompbnflcldabbghjo/html/nassh.html#profile-id:68af"
    #sshPwd = "P)O(I*U&"
    sshPwd = "Itaas4change"
    getPods = "kubectl get pods -n autotestorg-prod"
    masterline = "masterline.png"
    Utils.openWindow(sshAddr)
    messages = "messages.png"
    confirmClose = "confirmClose.png"
    wait(2)
    type(sshPwd + Key.ENTER)
    wait(2)
    type(getPods + Key.ENTER)
    wait(1)
    doubleClick(masterline)
    wait(2)
    type("kubectl exec -it --namespace=autotestorg-prod ")
    rightClick()
    wait(2)
    type(" -- redis-cli" + Key.ENTER)
    wait(2)
    type("get messages" + Key.ENTER)
    wait(2)
    hover(messages)
    wait(2)
    type("exit" + Key.ENTER)
    Utils.closeWindow()
    click(confirmClose)
    wait(5)

def checkMonitor(euPic):
    consoleButton = "consoleButton.png"
    detailsButton = "detailsButton.png"
    completeSign = "completeSign.png"
    monitorPanel = "monitorPanel.png"
    logPanel = "logPanel.png"
    axis = "xAxis.png"
    log = "log.png"
    hover(euPic)
    click(consoleButton)
    click(detailsButton)
    wait(completeSign, 100)
    hover(completeSign)
    click(monitorPanel)
    wait(axis, 100)
    hover(axis)
    click(logPanel)
    wait(log, 100)
    hover(log)

appName = "autoregm"
prodName = "autoapp"
frontendAddr = "http://9.112.249.90/frontend-autotestorg-prod/"

Utils.openWindow(Utils.addr)

Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
publishApp(Utils.euPic, appName, appName, Utils.testUserAcc, Utils.password)
deployTestApp()
deployProdApp(prodName)
Utils.logOutUser(Utils.euPic)

Utils.loginUser(Utils.oaAcc, Utils.oaPic, Utils.password)
approveProdApp()
Utils.logOutUser(Utils.oaPic)

Utils.loginUser(Utils.cusAcc, Utils.cusPic, Utils.password)
purchaseApp(appName)
sendAppMessages(Utils.cusPic)
accessApp(frontendAddr)
Utils.logOutUser(Utils.cusPic)

Utils.loginUser(Utils.euAcc, Utils.euPic, Utils.password)
checkMonitor(Utils.euPic)
Utils.logOutUser(Utils.euPic)

Utils.closeWindow()