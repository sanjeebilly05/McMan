from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
from tkinter import*

window = Tk()
window.geometry("420x402")
window.title("McMan")

icon = PhotoImage(file="images/mrDonald.png")
window.iconphoto(True, icon)
window.config(background = "#ffd700")
window.mainloop()

# with open("stuff.txt", "r") as f:
#     data = json.load(f)

# print("Welcome to McMan!\nUse this program to autocomplete your survey, and get your offer!")
# print("Don't worry about capital letters, we have that covered! :)")

# while True:
#     pounds = input("Enter the pounds of the meal: ").strip()
#     data["fill_in_boxes"]["pounds"]["default_message"] = pounds

#     pence = input("Enter the pence of your meal: ").strip()
#     data["fill_in_boxes"]["pence"]["default_message"] = pence

#     part1 = input("Enter your first code: ").strip().upper()
#     data["fill_in_boxes"]["code1"]["default_message"] = part1

#     part2 = input("Enter your second code: ").strip().upper()
#     data["fill_in_boxes"]["code2"]["default_message"] = part2

#     part3 = input("Enter your third code: ").strip().upper()
#     data["fill_in_boxes"]["code3"]["default_message"] = part3


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

# print(" - ".join([part1, part2, part3]))

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--incognito')
# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service = service, options = chrome_option)
# driver.get("https://www.mcdfoodforthoughts.com/")

# while True:
#     time.sleep(10)
#     for box in data["fill_in_boxes"].values():
#         try:
#             element = driver.find_element(By.XPATH, box["XPath"])
#             if "default_message" in box:
#                 element.send_keys(box["default_message"])
#         except:
#             print(f"{box["XPath"]} not found")


#     for option in data["options"].values():
#         try:
#             element = driver.find_element(By.XPATH, option["XPath"])
#             element.click()
#         except:
#             print(f"{option["XPath"]} not found")

#     next_button_XPath = data["buttons"]["next_button"]["XPath"]
#     try:
#         next_button = driver.find_element(By.XPATH, next_button_XPath)
#         next_button.click()
#     except:
#         print("I'm done")
#         break

# driver.quit()