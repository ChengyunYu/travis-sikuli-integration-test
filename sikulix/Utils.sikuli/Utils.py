from sikuli import *

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

#Dev
#addr = "http://marketplace.9.110.179.122.nip.io/"
#Test
#addr = "http://marketplace.9.112.232.156.nip.io/"
#Perf
#addr = "http://marketplace.9.112.234.93.nip.io/"
#Demo
addr = "http://marketplace-demo.9.112.244.252.nip.io/"
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
apiName = "autoapi"
yamlTitle = "tagtest"
apiVersion = "1.0.0"
testUserAcc = "testuser"