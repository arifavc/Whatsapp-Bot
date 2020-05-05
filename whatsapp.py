from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#options = Options()
#options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

name = input('Who should the message reach : ')
msg = input('Enter your message :  ')
count = int(input('Enter the count : '))

input('Press enter to send')

user = driver.find_element_by_xpath('//span[@title ="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')


for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
