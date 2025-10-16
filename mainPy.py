from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json

with open("stuff.txt", "r") as f:
    data = json.load(f)


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.mcdfoodforthoughts.com/")

code2_id = data["fill_in_boxes"]["code2"]["id"]
print(code2_id)

price_high_id = data["options"]["price_high"]["id"]
print(price_high_id)

next_button = data["buttons"]["next_button"]["id"]
print(next_button)

# def search_fill_in_box():

# def search_options():

# def search_button():
# waitTime = random.randint(1, 2)

# print("Welcome to McMan!\nUse this program to autocomplete your survey, and get your offer!")
# print("Don't worry about capital letters, we have that covered! :)")
# while True:
#     pounds = input("Enter the pounds of the meal: ").strip()
#     pence = input("Enter the pence of your meal: ").strip()
#     part1 = input("Enter your first code: ").strip().upper()
#     part2 = input("Enter your second code: ").strip().upper()
#     part3 = input("Enter your third code: ").strip().upper()

#     if len(pounds) < 4 and len(pence) < 3 and len(part1) == len(part2) == len(part3) == 4:
#         print("Your code is " + " - ".join([part1, part2, part3]) + " and you have spent " + "£" + pounds + "." + pence)
#         while True:
#             confirm = input("Is this code correct? (y/n): ").strip().lower()
#             if confirm == "y":
#                 print("Right! Let's continue on!")
#                 break
#             elif confirm == "n":
#                 print("Let's start again!")
#                 break
#             else:
#                 print("Invalid input, try again")
            
#         if confirm == "y":
#             break
#     else:
#         print("Your code or price isn't right, please try again")

# # print(" - ".join([part1, part2, part3]))

# part1 = "CLXW"
# part2 = "G7LM"
# part3 = "ZTTP"
# pounds = 4
# pence = 59

# time.sleep(waitTime)

# # Continue
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "NextButton"))
#     )
#     driver.find_element(By.ID, "NextButton").click()
# except:
#     driver.quit()

# time.sleep(waitTime)

# # Fill in code 1
# code1 = driver.find_element(By.ID, "CN1")
# code1.send_keys(part1)
# time.sleep(waitTime)

# # Fill in code 2
# code2 = driver.find_element(By.ID, "CN2")
# code2.send_keys(part2)
# time.sleep(waitTime)

# # Fill in code 3
# code3 = driver.find_element(By.ID, "CN3")
# code3.send_keys(part3)
# time.sleep(waitTime)

# # Fill in pounds
# poundBox = driver.find_element(By.ID, "AmountSpent1")
# poundBox.send_keys(pounds)
# time.sleep(waitTime)

# # Fill in pence
# penceBox = driver.find_element(By.ID, "AmountSpent2")
# penceBox.send_keys(pence)
# time.sleep(waitTime)

# # Start
# driver.find_element(By.ID, "NextButton").click() 
# time.sleep(waitTime)

# #Take Away
# driver.find_element(By.CLASS_NAME, "radioSimpleInput").click()
# time.sleep(waitTime)

# # Next
# driver.find_element(By.ID, "NextButton").click()
# time.sleep(waitTime)

# # Highly Satisfied
# driver.find_element(By.CLASS_NAME, "Opt5")
# time.sleep(waitTime)

# # Next
# driver.find_element(By.ID, "NextButton").click() 
# time.sleep(waitTime)

# # <label for="R000002.5" class="radioSimpleInput">‍</label>
# # The ease of placing your order
# driver.find_element(By.ID, "R000016.5").click()

# # The quality of your food and drink
# driver.find_element(By.ID, "R000008.5").click()

# # How well your order was packaged
# driver.find_element(By.ID, "R000144.5").click()

# # The friendliness of the staff
# driver.find_element(By.ID, "R000019.5").click()

# # The temperature of your food or drink
# driver.find_element(By.ID, "R000010.5").click()

# driver.quit()