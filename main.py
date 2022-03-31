from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


email = "tudorobre@gmail.com"
key = os.environ['password']

driver = webdriver.Chrome(executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe")
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&geoId=105773754&keywords=python%20developer&location=Bucharest%2C%20Romania"
driver.get(URL)

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]').click()

time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

time.sleep(0.5)
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys(email)

time.sleep(0.5)
password_form = driver.find_element(By.XPATH, '//*[@id="password"]')
password_form.send_keys(key)

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(1)

size = driver.get_window_size()
print(size)

driver.find_element(By.XPATH, '//*[@id="msg-overlay"]/div[1]/header/div[2]/button').click()

driver.set_window_size(1890, 1140)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scrolls to the end of the page by executing javascript code

time.sleep(1)
# height = document.body.scrollHeight
# print(height)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#TODO:1 Figure out how to scroll the right amount in the job scroll
#TODO:2 Get hold of now first element
#TODO:3 Press the save button of that job.

# element = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[2]/div/section[1]/div/div')
# # # driver.execute_script("arguments[0].scrollIntoView(true)", to_scroll)
# # driver.execute_script("window.scrollTo(0, document.body.1080);")
# driver.execute_script('js = (JavascriptExecutor) driver;'
#                       'js.executeScript("$(\"#ui-id-2\").animate({ scrollTop: \""+100*i+"px\" })");')

# for i in range(0, 25):
#     name = f"jobs-search-two-pane__job-card-container--viewport-tracking-{i}"
#     job = driver.find_element(By.CLASS_NAME, name)
#     print(job.text)
# # print(jobs.text)
jobs = driver.find_element(By.CLASS_NAME, "job-card-container--clickable") #WHY DOES THIS ONLY FIND THE FIRST 7-9 INSTANCES WHILE THE DOUBL CLASS FIND BELOW FINDS ALL OF THEM???
# for item in jobs:
#     item.click()
# print(len(jobs))

job_listings = driver.find_element(By.CLASS_NAME, "jobs-search-results__list").find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for item in job_listings:
    item.click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "jobs-save-button").click()
    time.sleep(0.5)



# print(len(job_listings))