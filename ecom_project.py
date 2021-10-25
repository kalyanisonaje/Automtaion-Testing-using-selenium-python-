import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# initialize webdriver
driver=webdriver.Chrome(r"C:\Users\Suyog\PycharmProjects\seleniumpythonproject\drivers\chromedriver.exe")

# open url and maximize window
driver.get("http://tutorialsninja.com/demo/")
driver.maximize_window()

# phones button
phones=driver.find_element_by_link_text("Phones & PDAs")
phones.click()
time.sleep(4)

# iphone
iphones=driver.find_element_by_link_text("iPhone")
iphones.click()
time.sleep(2)

# first picture
first_pic=driver.find_element_by_class_name("thumbnail")
first_pic.click()
time.sleep(2)

# next picture
next_click=driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')
# next_click.click()
# next_click.click()
# next_click.click()
# next_click.click()
# next_click.click()

for i in range (0,5):
    next_click.click()
    time.sleep(2)

# screenshot
driver.save_screenshot("screenshots#" + str(random.randint(0,101)) + '.png')

x_button=driver.find_element_by_xpath('//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)

#quantity
quantity=driver.find_element_by_id("input-quantity")
quantity.click()
time.sleep(2)

# clearquantity
quantity.clear()
time.sleep(1)
quantity.send_keys('0')
time.sleep(2)

# add to cart
add_to_button=driver.find_element_by_id("button-cart")
add_to_button.click()


laptopnotebook=driver.find_element_by_link_text("Laptops & Notebooks")
action=ActionChains(driver)
action.move_to_element(laptopnotebook).perform()
time.sleep(2)

laptopnotebook2=driver.find_element_by_link_text("Show All Laptops & Notebooks")
laptopnotebook2.click()

hp=driver.find_element_by_link_text("HP LP3065")
hp.click()
time.sleep(2)

# scroll
add_to_button_2=driver.find_element_by_id("button-cart")
add_to_button_2.location_once_scrolled_into_view
time.sleep(2)

# calender
calendar=driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calender=driver.find_element_by_xpath('//th[@class="next"]')
month_year=driver.find_element_by_xpath('//th[@class="picker-switch"]')

# year:2022 month:december
while month_year.text != 'December 2022':
    next_click_calender.click()
time.sleep(2)

# day 31
calendar_date=driver.find_element_by_xpath('//td[text()="31"]')
calendar_date.click()
time.sleep(2)

# add to button
add_to_button_2.click()

# checkout
go_to_cart=driver.find_element_by_id("cart-total")
go_to_cart.click()
time.sleep(2)

checkout=driver.find_element_by_xpath('//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

# click on guest account
guest=driver.find_element_by_xpath('//input[@value="guest"]')
guest.click()

# click continue
continue_1=driver.find_element_by_id("button-account")
continue_1.click()
time.sleep(2)

# scrolling
step_2=driver.find_element_by_xpath('//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

# first name
first_name=driver.find_element_by_id("input-payment-firstname")
first_name.click()
time.sleep(2)
first_name.send_keys('kalyani')
time.sleep(1)

# last name
last_name=driver.find_element_by_id("input-payment-lastname")
last_name.click()
time.sleep(2)
last_name.send_keys('sonaje')
time.sleep(1)

# email
email=driver.find_element_by_id("input-payment-email")
email.click()
time.sleep(2)
email.send_keys('sonaje@gmail.com')
time.sleep(1)

# telephone
telephone=driver.find_element_by_id("input-payment-telephone")
telephone.click()
time.sleep(2)
telephone.send_keys('7894561285')
time.sleep(1)

# address
address=driver.find_element_by_id("input-payment-address-1")
address.click()
time.sleep(2)
address.send_keys('b-cabin road')
time.sleep(1)

# city
city=driver.find_element_by_id("input-payment-city")
city.click()
time.sleep(2)
city.send_keys('Mumbai')
time.sleep(1)

#postcode
postcode=driver.find_element_by_id("input-payment-postcode")
postcode.click()
time.sleep(2)
postcode.send_keys('789456')
time.sleep(1)

# country
country=driver.find_element_by_id("input-payment-country")
dropdown_1=Select(country)
time.sleep(2)
dropdown_1.select_by_index(87)
time.sleep(1)

# region
region=driver.find_element_by_id("input-payment-zone")
dropdown_2=Select(region)
time.sleep(2)
dropdown_2.select_by_visible_text ('Hessen')
time.sleep(1)

# click on continue
continue_2=driver.find_element_by_id("button-guest")
continue_2.click()
time.sleep(1)

# click on continue
continue_3=driver.find_element_by_id("button-shipping-method")
continue_3.click()
time.sleep(2)

# accept terms and conditions
t_e=driver.find_element_by_xpath('//input[@name="agree"]')
t_e.click()
time.sleep(1)

# click on continue
continue_4=driver.find_element_by_id("button-payment-method")
continue_4.click()
time.sleep(3)

# final price
first_price=driver.find_element_by_xpath('//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("the final price is "+ first_price.text)
time.sleep(2)

# click on confirmation button
confirmation_button=driver.find_element_by_id("button-confirm")
confirmation_button.click()
time.sleep(1)

# success text
success_text=driver.find_element_by_xpath('//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(2)

driver.close()





