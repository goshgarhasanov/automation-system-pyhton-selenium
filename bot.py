import time
import db
from selenium import webdriver
myFakeData=db.getDB()
def getSite(userInfo):
    driver = webdriver.Edge(executable_path='msedgedriver.exe')
    driver.get("https://www.rezerwacje.lodzkie.eu/?lang=en#/?s=")
    driver.fullscreen_window()
    time.sleep(1)
    collectBtn = driver.find_elements_by_class_name(
        'queue-button')
    collectBtn[0].click()
    time.sleep(1)
    cityBtn=driver.find_elements_by_class_name('queue-button')
    if(userInfo['city']):
        cityBtn[2].click()
    else:
        cityBtn[3].click()
    time.sleep(2)

    #Main Program Plugin
    calendarRightBtn=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/button[2]').click()
    time.sleep(2)
    calendars = driver.find_elements_by_class_name('v-btn')
    for calendar in calendars:
        calendarClass=calendar.get_attribute('class')
        # calendar.click()
        print(calendarClass)

    time.sleep(1)
    stimes = driver.find_elements_by_class_name('xs6')
    stimes[userInfo['time']].click()
    time.sleep(1)
    fname = driver.find_element_by_css_selector("[aria-label='First name *']")
    fname.send_keys(userInfo['fname'])
    sname = driver.find_element_by_css_selector("input[aria-label='Surname *']")
    sname.send_keys(userInfo['sname'])
    phone = driver.find_element_by_css_selector("input[aria-label='Contact Phone Number *']")
    phone.send_keys(userInfo['phone'])
    email = driver.find_element_by_css_selector("input[aria-label='E-mail *']")
    email.send_keys(userInfo['email'])
    ctship = driver.find_element_by_css_selector("input[aria-label='Citizenship *']")
    ctship.send_keys(userInfo['ctship'])
    passportNumber = driver.find_element_by_css_selector("input[aria-label='Passport number *']")
    passportNumber.send_keys(userInfo['passportNumber'])
    captchaCode = driver.find_element_by_css_selector("[aria-label='Copy the text from the picture *']")
    captchaCode.send_keys('')
    c1 = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[8]/div/div/div[1]/div/div').click()
    c2 = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[9]/div/div/div[1]/div/div').click()
    c3 = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[10]/div/div/div[1]/div/div').click()
    captchaCode.send_keys('')
    time.sleep(2)

    submitBtn = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/button')



    while True:
        captcha=captchaCode.get_property('value')
        if(len(captcha)==5):
            # submitBtn.click()
            print("Register Success")
            submitBtn.click()
            break

getSite(myFakeData)



