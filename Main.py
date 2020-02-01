from selenium import webdriver
import time
browser = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
browser.get('https://www.godt.no/oppskrifter/alle')


python_button = browser.find_element_by_xpath("/html/body/div[1]/div[4]/div/section/div[2]/ul/li[1]/a")

python_button.click()
url = browser.current_url;

#On the selected site, finds the textbox and print out the descripton
browser.get(url)
element = browser.find_element_by_class_name("recipe-description")
bilde = browser.find_elements_by_xpath("/html/body/div[1]/div[4]/div/div/article/div[2]/ul/li/img/@src")

print(bilde.text)
#print(element.text)

#Show picture of the food.

#Show link for website and product. So the user can go to the website if he wants to make the food.





#print(url)







