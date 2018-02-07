from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = str(raw_input('who we spamming? '))
name = str(raw_input('whats ya ig username? '))
pw = str(raw_input('whats ya ig password? '))

driver = webdriver.Chrome()

driver.get('https://www.instagram.com')

sleep(3)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button').click()

driver.find_element_by_name("email").send_keys(name)
driver.find_element_by_name("pass").send_keys(pw)
driver.find_element_by_name("login").click()

sleep(3)

body_elem = driver.find_element_by_tag_name('body')
body_elem.send_keys(Keys.END)
body_elem.send_keys(Keys.HOME)
print 'okay were in instagram succesfully.'

##find all the heart links on your newsfeed

# hearts = driver.find_elements_by_xpath('//a[contains(@class, "_eszkz _l9yih")]')
#
# if len(hearts) > 0:
#     print 'Oh neat, we found {} hearts to like!'.format(len(hearts))
# else:
#     print 'didn\'t find any hearts to like :('
#
# for i, heart in enumerate(hearts):
#     print '{}/{}'.format(i+1, len(hearts))
#     heart.click()
#     sleep(2)

# search for a specific profile
element = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
element.send_keys(user)
sleep(3)
element.send_keys(Keys.RETURN)
element.send_keys(Keys.RETURN)
sleep(3)

# find all the pictures on someone's instagram
pics = driver.find_elements_by_xpath('//div[contains(@class, "_mck9w _gvoze _f2mse")]')

if len(pics) == 0:
    print 'There are {} likable things on this person\'s profile'.format(len(pics))
else:
    print 'There are {} likable things on this person\'s profile'.format(len(pics))
    for i, pic in enumerate(pics):
        print '{}/{}'.format(i+1, len(pics))
        pic.click()
        sleep(2)
        driver.find_element_by_xpath('//a[contains(@class, "_eszkz _l9yih")]').click()
        sleep(2)
        driver.find_element_by_xpath('//a[contains(@class, "_p6oxf _6p9ga")]').click()
        sleep(2)
        input = driver.find_element_by_xpath('//textarea[contains(@class, "_bilrf")]')
        input.send_keys("hi {}!".format(user))
        input.send_keys(Keys.RETURN)
        sleep(4)
        driver.find_element_by_xpath('//button[contains(@class, "_dcj9f")]').click()
        sleep(2)

driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
#
# def login():
#
# 	browser = webdriver.Firefox()
# 	browser.get('https://instagram.com/accounts/login')
# 	'''
# 	When page loads the Login Form Container is not loaded immediately, that is why we need to do a smart wait,
# 	the following waits up to 15 seconds if the element not found immediately.
# 	'''
# 	wait = WebDriverWait(browser, 15)
# 	wait.until(lambda browser: browser.find_element_by_css_selector('.-cx-PRIVATE-Login__formContainer'))
#
# 	username_field = browser.find_element_by_name("username").send_keys("username")
# 	password_field = browser.find_element_by_name("password").send_keys("password")
# 	login_button = browser.find_element_by_css_selector('.-cx-PRIVATE-LoginForm__loginButton')
# 	login_button.click()
#
#  	browser.quit()
#
# login()
